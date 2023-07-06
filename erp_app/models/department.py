from flask_sqlalchemy import SQLAlchemy
from erp_app import db

class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    users = db.relationship('User', backref='department', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Department {}>'.format(self.name)