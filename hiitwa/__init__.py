from flask import Flask
from hiitwa.controller import main_blueprint, auth_blueprint, workout_blueprint
from hiitwa.models import db, login_manager


def create_app():
    """
    Function that creates flask app and initializes it
    """
    # Create app
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(main_blueprint.app)
    app.register_blueprint(auth_blueprint.app)
    app.register_blueprint(workout_blueprint.app)

    # Attach config file with secret
    app.config.from_pyfile("config/app.cfg", silent=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

    # Init DB

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"
    return app
