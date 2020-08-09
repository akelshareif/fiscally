""" Application Factory File """
# Contains application factory function and tells Python to treat application directory as a package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db is globally accessible
db = SQLAlchemy()


def create_app(test_config=None):
    """ Creates and configures Flask app instance """

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize db
    db.app = app
    db.init_app(app)

    with app.app_context():
        # Import blueprints
        from .home import home
        from .users import users
        from .auth import auth

        # Create db tables
        db.create_all()

        # Register blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(users.users_bp)
        app.register_blueprint(auth.auth_bp)

        return app
