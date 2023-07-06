from flask_login import login_user, logout_user
from erp_app.models.user import User
from erp_app.models.authentication import Authentication
from erp_app import db

def authenticate_user(username, password, department):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        auth = Authentication.query.filter_by(user_id=user.id, department=department).first()
        if auth:
            login_user(user)
            return True
    return False

def logout():
    logout_user()