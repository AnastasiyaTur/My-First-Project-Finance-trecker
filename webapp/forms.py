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
    transaction_type = RadioField('Transaction type',
                                  choices=['Expenses', 'Income', 'Transfer'],
                                  render_kw={"class": "form-check-input"})
    description = TextAreaField('Description', validators=[DataRequired()],
                                render_kw={"class": "form-control"})
    account_type = SelectField('Account type',
                               choices=['Cash', 'Card', 'Bank'],
                               render_kw={"class": "custom-select"})
    amount = FloatField('Amount', validators=[DataRequired()],
                        render_kw={"class": "form-control"})
    date_of_transaction = DateField('Date', validators=[DataRequired()],
                                    format='%Y-%m-%d',
                                    render_kw={"class": "form-control"})
    category_name = SelectField('Category',
                                choices=['Salary', 'Groceries', 'Gift', 'Cafe',
                                         'Transportation', 'Phone', 'Workout'],
                                render_kw={"class": "custom-select"})
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
