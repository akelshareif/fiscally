from flask import Blueprint

home = Blueprint('home', __name__)


@home.route('/')
def root():
    """ Main root route of application """

    return 'This is the home page.'
