from flask_wtf import FlaskForm
from wtforms import (DateField, FloatField, RadioField,
                     SelectField, StringField, SubmitField)
from wtforms.validators import DataRequired


class AddTransaction(FlaskForm):
    # Create form for add a new transaction
    budget_type = RadioField('Transaction type',
                             choices=[(1, 'Expenses'), (2, 'Income')])
    description = StringField('Description')
    account_type = SelectField(
        'Account type', coerce=int, validate_choice=False,
        choices=[(6, 'Cash'), (7, 'Card MasterCard'), (8, 'Bank')])
    amount = FloatField('Amount', validators=[DataRequired()],
                        render_kw={"class": "form-control"})
    date_of_transaction = DateField('Date', validators=[DataRequired()],
                                    format='%Y-%m-%d',
                                    render_kw={"class": "form-control"})
    category_name = SelectField(
        'Category',
        choices=[(5, 'Salary'), (12, 'Groceries'),
                 (9, 'Gifts'), (13, 'Cafe'),
                 (4, 'Transportation'), (6, 'Investment'),
                 (10, 'Workout')])
    submit = SubmitField('Add', render_kw={"class": "btn btn-primary"})
