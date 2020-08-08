from flask import Blueprint, render_template

home = Blueprint('home', __name__, template_folder='templates')


@home.route('/')
def home_page():
    """ Main root route of application """

    return render_template('home/home.jinja')
