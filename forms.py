from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import Optional, InputRequired


class GenericForm(FlaskForm):
    """ This is a template """

    # Add Form fields here
    testField = StringField('Field Name', validators=[Optional()])
