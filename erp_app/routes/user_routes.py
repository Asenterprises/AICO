from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from erp_app.models.user import User
from erp_app.services.user_service import get_user_by_username, create_user

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data.get('username')
    password = data.get('password')

    user = get_user_by_username(username)
    if user and check_password_hash(user.password, password):
        login_user(user)
        flash('login_success')
        return redirect(url_for('dashboard'))
    else:
        flash('login_failure')
        return redirect(url_for('login'))

@user_routes.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@user_routes.route('/register', methods=['POST'])
def register():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    department_id = data.get('department_id')

    user = get_user_by_username(username)
    if not user:
        create_user(username, password, department_id)
        flash('registration_success')
        return redirect(url_for('login'))
    else:
        flash('registration_failure')
        return redirect(url_for('register'))