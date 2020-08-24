from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length


class EditAccountForm(FlaskForm):
    """ Form to edit user account """

    first_name = StringField('First Name', validators=[InputRequired(
        message='First name is required.'), Length(max=20)])
    last_name = StringField('Last Name', validators=[InputRequired(
        message='Last name is required.'), Length(max=20)])
    email = StringField('Email', validators=[InputRequired(
        message='Enter a valid email.'), Email(message="Enter a valid email")])
