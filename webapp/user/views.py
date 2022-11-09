from database import db_session
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user
from webapp.user.forms import LoginForm, SignUpForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route("/login")
def login():
    # Page with a form for user authorization
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Authorization"
    login_form = LoginForm()
    return render_template('user/login.html',
                           page_title=title,
                           form=login_form)


@blueprint.route("/process-login", methods=['POST'])
def process_login():
    # Process of user authorization
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Login successfully')
            return redirect(url_for('index'))
    flash('The entered data is incorrect')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    # Logout the user from the app
    logout_user()
    flash('You successfully logged out')
    return redirect(url_for('index'))


@blueprint.route('/signup')
def sign_up():
    # # Page with a form for user registration
    title = "Registration"
    sign_up_form = SignUpForm()
    return render_template('user/signup.html', page_title=title,
                           form=sign_up_form)


@blueprint.route("/process-signup", methods=['GET', 'POST'])
def process_signup():
    # Process of user registration
    form = SignUpForm()

    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        print(user)
        if user is None:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db_session.add(user)
            db_session.commit()
            login_user(user)
            flash('SignUp successfully')
            return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Error in field {getattr(form, field).label.text}: '
                      f'{error}')
    return redirect(url_for('user.sign_up'))
