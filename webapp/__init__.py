from flask import Flask, flash, redirect, render_template, url_for
from flask_login import LoginManager, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy

from webapp.forms import LoginForm
from webapp.models import  User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    #db = SQLAlchemy(app)  здесь пыталась связать, но по итогу ошибка
    #db.init_app(app)

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
        title = "Authorization"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)


    @app.route("/process-login", methods=['POST'])
    def process_login():
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Login successfully')
                return redirect(url_for('index'))

        flash('The entered data is incorrect')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('You successfully logged out')
        return redirect(url_for('index'))

    return app


