# App packages
import os
from flask import Flask
from models import db, connect_db

# Blueprint imports
from home.home import home
from users.users import users
from auth.auth import auth

# App config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DB_URL', 'postgresql:///fiscally')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

# DB connection and table creation
connect_db(app)
db.create_all()


# Blueprint registrations
app.register_blueprint(home)
app.register_blueprint(users)
app.register_blueprint(auth)
