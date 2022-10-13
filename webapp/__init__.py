from flask import Flask, flash, redirect, render_template, url_for
from flask_login import LoginManager, current_user, login_user, logout_user

from database import db_session
from webapp.forms import LoginForm, SignUpForm
from webapp.models import  User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route("/")
    def index():
        title = "Finance trecker"
        description = "Here is the description of the application"    
        return render_template('index.html', page_title=title, description=description)


    @app.route("/login")
    def login():
        if current_user.is_authenticated:
            return redirect (url_for('index'))        
        title = "Authorization"        
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)


    @app.route("/process-login", methods=['POST'])
    def process_login():
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter(User.email == form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash('Login successfully')
                return redirect(url_for('index'))
        
        flash('The entered data is incorrect')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('You successfully logged out')
        return redirect(url_for('index'))

    @app.route('/signup')
    def sign_up():
        title = "Registration"
        sign_up_form = SignUpForm()
        return render_template('signup.html', page_title=title, form=sign_up_form)

    
    @app.route("/process-signup", methods=['GET','POST'])
    def process_signup():
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
                return redirect(url_for('index'))

        flash("A user already exists with that email address.")
        return redirect(url_for('signup'))        
        

    return app
