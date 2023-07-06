from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize Flask app
app = Flask(__name__)

# Load configurations
app.config.from_object('erp_app.config')

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import routes
from erp_app.routes import user_routes, department_routes, authentication_routes, noodle_manufacturing_process_routes

# Import models
from erp_app.models import user, department, authentication, noodle_manufacturing_process

# Create database tables
db.create_all()