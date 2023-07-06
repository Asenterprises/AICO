from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from erp_app.models.user import User
from erp_app.services.authentication_service import authenticate_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.', 'login_failure')
        return redirect(url_for('auth.login'))

    if not authenticate_user(user, request.form.get('department')):
        flash('You are not authorized to access this department.', 'authentication_failure')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    flash('Successfully logged in.', 'login_success')
    return redirect(url_for('main.dashboard'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))