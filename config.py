""" Flask configurations """
from os import environ, path
from dotenv import load_dotenv

base_dir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(base_dir, '.env'))


class Config:
    """ Base configuration """

    SECRET_KEY = environ.get('SECRET_KEY')
    GOOGLE_CLIENT_ID = environ.get('CLIENT_ID')
    GOOGLE_CLIENT_SECRET = environ.get('CLIENT_SECRET')
    SENDGRID_API_KEY = environ.get('SENDGRID_API_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProdConfig(Config):
    """ Production Configuration """

    DEBUG = False
    TESTING = False
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class DevConfig(Config):
    """ Development Configuration """

    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class TestConfig(Config):
    """ Testing Configuration """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
