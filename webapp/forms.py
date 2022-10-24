from flask_wtf import FlaskForm
from webapp.models import User
from wtforms import (BooleanField, DateField, EmailField, FloatField,
                     PasswordField, RadioField, SelectField, StringField,
                     SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    # Create Login Form
    username = StringField('Username', validators=[DataRequired()],
                           render_kw={"class": "form-control"})
    email = EmailField('Email', validators=[Email()],
                       render_kw={"class": "form-control"})
    password = PasswordField('Password', validators=[DataRequired()],
                             render_kw={"class": "form-control"})
    remember_me = BooleanField('Remember me', default=True,
                               render_kw={"class": "form-check-input"})
    submit = SubmitField('Log in', render_kw={"class": "btn btn-primary"})


class SignUpForm(FlaskForm):
    # Create form for registration a new user
    username = StringField('Username', validators=[DataRequired()],
                           render_kw={"class": "form-control"})
    email = EmailField('Email', validators=[DataRequired(), Email()],
                       render_kw={"class": "form-control"})
    password = PasswordField('Password', validators=[DataRequired()],
                             render_kw={"class": "form-control"})
    password2 = PasswordField('Repeat password', validators=[DataRequired(),
                              EqualTo('password')],
                              render_kw={"class": "form-control"})
    submit = SubmitField('Sign up', render_kw={"class": "btn btn-primary"})

    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError('A user already exists with that email '
                                  'address.')


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
    cancel = SubmitField('Cancel', render_kw=({"class": "btn btn-secondary"},
                                              {'formnovalidate': True}))


class CreateAccount(FlaskForm):
    # Create a new account
    account_name = StringField('Account name', validators=[DataRequired()],
                               render_kw={"class": "form-control"})
    amount = FloatField('Amount', validators=[DataRequired()],
                        render_kw={"class": "form-control"})
    submit = SubmitField('Add', render_kw={"class": "btn btn-primary"})


class CreateCategory(FlaskForm):
    # Create a new category
    category_name = StringField('Category name', validators=[DataRequired()],
                                render_kw={"class": "form-control"})
    budget_type = RadioField('Budget type',
                             choices=[(1, 'Expenses'), (2, 'Income')])
    submit = SubmitField('Add', render_kw={"class": "btn btn-primary"})
