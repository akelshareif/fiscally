from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired


class BillForm(FlaskForm):
    """ Add bill form """

    bill_name = StringField('Bill Name', validators=[
                            InputRequired(message="You must add a bill name.")])

    bill_due_date = DateField('Pay Date', format='%Y-%m-%d',
                              validators=[InputRequired(message="You must select a bill due date.")])

    bill_amount = DecimalField('Bill Amount', validators=[
                               InputRequired(message="You must enter a bill amount.")])
