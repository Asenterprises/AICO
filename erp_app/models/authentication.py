from flask_login import UserMixin
from erp_app import db

class Authentication(UserMixin, db.Model):
    __tablename__ = 'authentication'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

    def __init__(self, user_id, department_id):
        self.user_id = user_id
        self.department_id = department_id

    def __repr__(self):
        return f'<Authentication User_id={self.user_id}, Department_id={self.department_id}>'