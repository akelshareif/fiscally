from flask import Blueprint, render_template, request, redirect
from .models import db, GenericModel
from .forms import GenericForm


# Initialize blueprint
home_bp = Blueprint('home', __name__, template_folder='templates')


# Home page endpoints


@home_bp.route('/', methods=['GET', 'POST'])
def home_page():
    """ Main root route of application """

    form = GenericForm()

    if form.validate_on_submit():
        newp = GenericModel(name=form.name.data)
        db.session.add(newp)
        db.session.commit()
        return redirect('/')

    return render_template('home/home.jinja', form=form)
