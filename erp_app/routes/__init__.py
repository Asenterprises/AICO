from flask import Blueprint

from .user_routes import user_routes
from .department_routes import department_routes
from .authentication_routes import authentication_routes
from .noodle_manufacturing_process_routes import noodle_manufacturing_process_routes

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Welcome to the Noodle Manufacturing ERP!"

# Registering the blueprints
def register_routes(app):
    app.register_blueprint(user_routes)
    app.register_blueprint(department_routes)
    app.register_blueprint(authentication_routes)
    app.register_blueprint(noodle_manufacturing_process_routes)
    app.register_blueprint(main)