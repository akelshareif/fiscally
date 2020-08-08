from flask import Blueprint

users = Blueprint('users', __name__, url_prefix='/user',
                  template_folder='templates', static_folder='static', static_url_path='assets')


@users.route('/')
def user_profile():
    """ Displays profile for logged-in user """

    return 'This is a user profile'
