""" Application Factory File """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from authlib.integrations.flask_client import OAuth


# Instantiate a globally accessible SQLAlchemy instance
db = SQLAlchemy()

# Instantiate Flask-SqlAlchemy database migration
migrate = Migrate()

# Instantiate flask-login
login_manager = LoginManager()

# Instantiate OAuth
oauth = OAuth()


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

    # Initialize all extensions
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    oauth.init_app(app)

    with app.app_context():
        # Import blueprints
        from .home import home
        from .user import user
        from .auth import auth
        from .pay import pay
        from .bills import bills
        from .savings import savings
        from .taxee_api import taxee

        # Register blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(user.user_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(pay.pay_bp)
        app.register_blueprint(bills.bills_bp)
        app.register_blueprint(savings.savings_bp)
        app.register_blueprint(taxee.taxee_bp)

        return app
