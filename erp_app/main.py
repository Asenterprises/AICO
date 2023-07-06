from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize Flask app
app = Flask(__name__)

# Load configurations
app.config.from_object('erp_app.config')

# Initialize SQLAlchemy with app
db = SQLAlchemy(app)

# Initialize LoginManager with app
login_manager = LoginManager(app)

# Import routes
from erp_app.routes import user_routes, department_routes, authentication_routes, noodle_manufacturing_process_routes

# Import models
from erp_app.models import user, department, authentication, noodle_manufacturing_process

# Create all database tables
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)