""" Application Factory File """
# Contains application factory function and tells Python to treat application directory as a package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# Initialize a globally accessible SQLAlchemy instance
db = SQLAlchemy()

# Initialize Flask-SqlAlchemy database migration and Flask-Script manager
migrate = Migrate()


def create_app(is_testing=False):
    """ Creates and configures Flask app instance """

    app = Flask(__name__, instance_relative_config=False)

    # Dynamic configuration selection
    if is_testing is not False:
        app.config.from_object('config.TestConfig')
    elif app.config['ENV'] == 'production':
        app.config.from_object('config.ProdConfig')
    else:
        app.config.from_object('config.DevConfig')

    # Initialize all plugins
    db.app = app
    db.init_app(app)

    migrate.init_app(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    with app.app_context():
        # Import blueprints
        from .home import home

        # Create db tables
        # db.create_all()

        # Register blueprints
        app.register_blueprint(home.home_bp)

        return app
