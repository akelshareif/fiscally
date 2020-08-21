""" All pay related forms """

from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, RadioField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Optional, NumberRange
from .state_dict import states


class PaycheckForm(FlaskForm):
    """ Add/edit paycheck form """

    pay_frequency = RadioField('Pay Frequency', choices=[(52, 'Weekly'), (26, 'Bi-Weekly'), (24, 'Semi-Monthly'), (
        12, 'Monthly')], validators=[InputRequired(message="You must select a pay frequency.")])

    pay_date = DateField('Pay Date', format='%Y-%m-%d',
                         validators=[InputRequired()])

    gross_pay = DecimalField('Gross Pay', places=2, validators=[
                             InputRequired(message="You must enter your gross pay."), NumberRange(min=0, message="Gross pay cannot be less than zero.")])

    filing_status = RadioField('Filing Status', choices=[('single', 'Single'), ('married', 'Married'), ('married_separately', 'Married Filing Separately'), (
        'head_of_household', 'Head of Household')], validators=[InputRequired(message="You must select your filing status.")])

    state = SelectField('State', choices=list(states.items()), validators=[InputRequired(
        message="You must select the state which you've worked in.")])

    exemptions = IntegerField('Number of Exemptions', validators=[
                              Optional(), NumberRange(min=0, message="Gross pay cannot be less than zero.")])

    pre_tax_deductions = DecimalField(
        'Pre-Tax Deductions', places=2, validators=[Optional(), NumberRange(min=0, message="Gross pay cannot be less than zero.")])


class SalaryGrossPayForm(FlaskForm):
    """ Form to calculate gross salary """

    salary = DecimalField('Annual Salary', places=2, validators=[
                          InputRequired(message="You must enter your annual salary.")])
    pay_frequency = RadioField('Pay Frequency', choices=[(52, 'Weekly'), (26, 'Bi-Weekly'), (24, 'Semi-Monthly'), (
        12, 'Monthly')], validators=[InputRequired(message="You must select a pay frequency.")])
