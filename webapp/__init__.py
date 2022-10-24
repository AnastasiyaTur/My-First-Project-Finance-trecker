from database import db_session
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, current_user, login_user, logout_user
from webapp.forms import AddTransaction, CreateAccount, CreateCategory, LoginForm, SignUpForm
from webapp.models import AccountType, СategoryName, Transaction, User


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
        return render_template('index.html', page_title=title)

    @app.route("/login")
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
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
        return render_template('signup.html', page_title=title,
                               form=sign_up_form)

    @app.route("/process-signup", methods=['GET', 'POST'])
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
                return redirect(url_for('login'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'Error in field {getattr(form, field).label.text}: '
                          f'{error}')
        return redirect(url_for('sign_up'))

    @app.route('/new_transaction')
    def new_transaction():
        title = "Add new_transaction"
        transaction_form = AddTransaction()
        return render_template('transaction.html', page_title=title,
                               form=transaction_form)

    @app.route("/process-create-transaction", methods=['GET', 'POST'])
    def process_create_transaction():
        form = AddTransaction()    
        
        date = request.form['date_of_transaction']         
        category_name = request.form['select_category']
        account_type = request.form['select_account']
        budget_type = request.form['inlineRadioOptions']        
        new_transaction = Transaction(
            account_type_id=account_type,
            budget_type_id=budget_type,
            category_name_id=category_name,
            amount=form.amount.data,
            date_of_transaction=date,
            description=form.description.data)     
        db_session.add(new_transaction)
        db_session.commit()
        flash('A new transaction create successfully')
        return redirect(url_for('index'))
        
        flash('An error has occurred. Data not saved')
        return redirect(url_for('new_transaction'))

    @app.route('/accounts')
    def accounts():
        title = "Accounts"        
        return render_template('accountpage.html', page_title=title)

    @app.route('/create_account')
    def create_account():
        title = "Create account"
        create_account_form = CreateAccount()
        return render_template('create_account.html', page_title=title,
                               form=create_account_form)

    @app.route("/process_create_account", methods=['GET', 'POST'])
    def process_create_account():
        form = CreateAccount()

        if form.validate_on_submit():
            account = AccountType.query.filter(AccountType.name == form.account_name.data).first()
            print(account)
            if account is None:
                account = AccountType(name=form.account_name.data, amount=form.amount.data)
                db_session.add(account)
                db_session.commit()
                flash('Create account successfully')
                return redirect(url_for('accounts'))
        flash('An error has occurred. Data not saved')
        return redirect(url_for('create_account'))

    @app.route('/category_income')
    def category_income():
        # title = "Categories"
        return render_template('category_income.html')

    @app.route('/category_expenses')
    def category_expenses():
        # title = "Categories"
        return render_template('category_expenses.html')

    @app.route('/create_category')
    def create_category():
        title = "Create category"
        create_category_form = CreateCategory()
        return render_template('create_category.html', page_title=title,
                               form=create_category_form)

    @app.route("/process_create_category", methods=['GET', 'POST'])
    def process_create_category():
        form = CreateCategory()
        
        category = СategoryName.query.filter(СategoryName.name == form.category_name.data).first()
        print(category)
        if category is None:
            type = request.form['inlineRadioOptions']
            category = СategoryName(name=form.category_name.data, budget_type_id=type)
            db_session.add(category)
            db_session.commit()
            flash('Create category successfully')
            return redirect(url_for('category_expenses'))
        flash('An error has occurred. Data not saved')
        return redirect(url_for('create_category'))

    @app.route('/budget_expenses')
    def budget_expenses():
        # title = "Budget"
        return render_template('budget_expenses.html')

    @app.route('/budget_income')
    def budget_income():
        # title = "Budget"
        return render_template('budget_income.html')

    return app
