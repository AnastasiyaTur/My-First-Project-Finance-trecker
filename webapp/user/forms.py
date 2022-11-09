from flask_wtf import FlaskForm
from webapp.user.models import User
from wtforms import (BooleanField, EmailField, PasswordField, StringField,
                     SubmitField)
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
