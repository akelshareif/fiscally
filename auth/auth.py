from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, url_prefix='/auth',
                 template_folder='templates')


@auth.route('/')
def auth_route():

    return 'This is from auth'
