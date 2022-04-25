"""
 * FILENAME: [hww-app]
 * AUTHOR: [Team Workout App]
 * COURSE: [CMSC 495 7383]
 * PROFESSOR: [Jeff Sanford]
 * CREATEDATE: [04/16/2022]

"""
from flask import Flask

from db import db
from controller import main_blueprint, auth_blueprint, workout_blueprint


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

    # Init DB
    db.init_app(app)

    # Attach config file with secret
    app.config.from_pyfile('config/app.cfg', silent=True)

    return app


# run file with python3 cmd
if __name__ == "__main__":
    create_app()
