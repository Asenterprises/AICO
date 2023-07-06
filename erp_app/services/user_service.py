from flask_login import login_user, logout_user
from erp_app.models.user import User
from werkzeug.security import check_password_hash

def register_user(username, password, department):
    user = User(username=username, password=password, department=department)
    db.session.add(user)
    db.session.commit()

def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return True
    return False

def logout_user():
    logout_user()