from database import db_session
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, current_user, login_user, logout_user
from webapp.forms import (AddTransaction, CreateAccount, CreateCategory,
                          LoginForm, SignUpForm)
from webapp.models import AccountType, BudgetType, СategoryName, Transaction, User
from webapp.reports import pie_chart_expenses, pie_chart_income, bar_chart_expenses, bar_chart_income
from webapp.account_transactions import account_transactions


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
        categories_list = СategoryName.query.filter_by().all()
        accounts_list = AccountType.query.filter_by().all()
        return render_template('transaction.html', page_title=title,
                               form=transaction_form,
                               categories_list=categories_list,
                               accounts_list=accounts_list)

    @app.route("/process-create-transaction", methods=['GET', 'POST'])
    def process_create_transaction():
        try:
            new_transaction = Transaction(
                account_type_id=request.form['select_account'],
                budget_type_id=request.form['inlineRadioOptions'],
                category_name_id=request.form['select_category'],
                amount=request.form['amount'],
                date_of_transaction=request.form['date_of_transaction'],
                description=request.form['description'])
            db_session.add(new_transaction)
            db_session.commit()
            account_transactions()
            flash('A new transaction create successfully')
            return redirect(url_for('index'))
        except Exception as e:
            print(e)
        flash('An error has occurred. Data not saved')
        return redirect(url_for('new_transaction'))

    @app.route('/accounts')
    def accounts():
        title = "Accounts"
        accounts_list = AccountType.query.filter_by().all()
        total_amount = 0
        for account in accounts_list:
            total_amount += account.amount
        return render_template('account_page.html',
                               page_title=title,
                               accounts_list=accounts_list,
                               total_amount=total_amount)

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

    @app.route('/account/<int:id>/edit', methods=['GET', 'POST'])
    def account_edit(id):
        account = AccountType.query.get(id)
        if request.method == "POST":
            account.name = request.form['name']
            account.amount = request.form['amount']
            try:
                db_session.commit()
                return redirect(url_for('accounts'))
            except Exception as e:
                print(f'Error {e}')
        else:
            return render_template("edit_account.html", account=account)

    @app.route('/account/<int:id>/delete', methods=['GET', 'POST'])
    def account_delete(id):
        account = AccountType.query.filter_by(id=id).first()
        try:
            db_session.delete(account)
            db_session.commit()
            flash('Delete account successfully')
            return redirect(url_for('accounts'))
        except Exception as e:
            print(f'Error {e}')
            flash('An error has occurred. The account has not been removed.')
            return redirect(url_for('accounts'))

    @app.route('/category_income')
    def category_income():
        categories_income_list = СategoryName.query.filter_by(budget_type_id=2).all()
        return render_template('category_income.html',
                               categories_income_list=categories_income_list)

    @app.route('/category_expenses')
    def category_expenses():
        categories_expenses_list = СategoryName.query.filter_by(budget_type_id=1).all()
        return render_template(
            'category_expenses.html',
            categories_expenses_list=categories_expenses_list)

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
            if type == '1':
                category = СategoryName(name=form.category_name.data, budget_type_id=type)            
                db_session.add(category)
                db_session.commit()
                flash('Create category successfully')
                return redirect(url_for('category_expenses'))
            else:
                category = СategoryName(name=form.category_name.data, budget_type_id=type)            
                db_session.add(category)
                db_session.commit()
                flash('Create category successfully')
                return redirect(url_for('category_income'))

        flash('An error has occurred. Data not saved')
        return redirect(url_for('create_category')) 

    @app.route('/category/<int:id>/delete', methods=['GET', 'POST'])
    def category_delete(id):
        category = СategoryName.query.filter_by(id=id).first()
        if category.budget_type_id == 1:
            try:
                db_session.delete(category)
                db_session.commit()
                flash('Delete category successfully')
                return redirect(url_for('category_expenses'))
            except Exception as e:
                print(f'Error {e}')
                flash('An error has occurred. The category has not been removed.')
                return redirect(url_for('category_expenses'))
        else:
            try:
                db_session.delete(category)
                db_session.commit()
                flash('Delete category successfully')
                return redirect(url_for('category_income'))
            except Exception as e:
                print(f'Error {e}')
                flash('An error has occurred. The category has not been removed.')
                return redirect(url_for('category_income'))

    @app.route("/category/<int:id>/edit", methods=['GET', 'POST'])
    def category_edit(id):
        category = СategoryName.query.get(id)
        if request.method == "POST":
            category.name = request.form['name']
            category.budget_type_id = request.form['inlineRadioOptions']
            if category.budget_type_id == '1':
                try:
                    db_session.commit()
                    return redirect(url_for('category_expenses'))
                except Exception as e:
                    print(f"Error {e}")
            else:
                try:
                    db_session.commit()
                    return redirect(url_for('category_income'))
                except Exception as e:
                    print(f"Error {e}")
        else:
            return render_template("edit_category.html", category=category)

    @app.route('/budget_expenses')
    def budget_expenses():
        # title = "Budget"
        categories_expenses_list = СategoryName.query.filter_by(budget_type_id=1).all()
        transaction_list = Transaction.query.order_by(Transaction.date_of_transaction.desc()).filter_by().all()        
        total_amount = 0
        for category in categories_expenses_list:
            for transaction in transaction_list:
                if category.id == transaction.category_name_id:
                    total_amount += transaction.amount

        return render_template(
            'budget_expenses.html',
            categories_expenses_list=categories_expenses_list,
            transaction_list=transaction_list,
            total_amount=total_amount)

    @app.route('/budget_income')
    def budget_income():
        # title = "Budget"
        categories_income_list = СategoryName.query.filter_by(budget_type_id=2).all()
        transaction_list = Transaction.query.filter_by().all()
        total_amount = 0
        for category in categories_income_list:
            for transaction in transaction_list:
                if category.id == transaction.category_name_id:
                    total_amount += transaction.amount

        return render_template(
            'budget_income.html',
            categories_income_list=categories_income_list,
            transaction_list=transaction_list,
            total_amount=total_amount)

    @app.route('/budget/<int:id>/edit', methods=['GET', 'POST'])
    def budget_edit(id):
        transaction = Transaction.query.get(id)
        if request.method == "POST":
            # transaction.category_name_id = request.form['name']
            # transaction.account_type_id = request.form['account']
            transaction.amount = request.form['amount']
            transaction.date_of_transaction = request.form['date']
            transaction.description = request.form['description']
            if transaction.budget_type_id == 1:
                try:
                    db_session.commit()
                    return redirect(url_for('budget_expenses'))
                except Exception as e:
                    print(f'Error {e}')
            else:
                try:
                    db_session.commit()
                    return redirect(url_for('budget_income'))
                except Exception as e:
                    print(f'Error {e}')
        else:
            return render_template("edit_budget.html", transaction=transaction)


    @app.route('/budget/<int:id>/delete', methods=['GET', 'POST'])
    def budget_delete(id):
        transaction = Transaction.query.filter_by(id=id).first()
        try:
            db_session.delete(transaction)
            db_session.commit()
            flash('Delete transaction successfully')
            return redirect(url_for('budget_expenses'))
        except Exception as e:
            print(f'Error {e}')
            flash('An error has occurred. The account has not been removed.')
            return redirect(url_for('budget_expenses'))


    @app.route('/reports')
    def reports():
        title = "Reports"
        return render_template('reports.html', page_title=title)

    @app.route('/expenses_pie_chart', methods=['GET', 'POST'])
    def expenses_pie_chart():
        try:
            pie_chart_expenses()
            return redirect(url_for('reports'))
        except Exception as e:
            print(f"Error {e}")            
            return redirect(url_for('reports'))

    @app.route('/income_pie_chart', methods=['GET', 'POST'])
    def income_pie_chart():
        try:
            pie_chart_income()
            return redirect(url_for('reports'))
        except Exception as e:
            print(f"Error {e}")            
            return redirect(url_for('reports'))

    @app.route('/expenses_bar_chart', methods=['GET', 'POST'])
    def expenses_bar_chart():
        try:
            bar_chart_expenses()
            return redirect(url_for('reports'))
        except Exception as e:
            print(f"Error {e}")            
            return redirect(url_for('reports'))

    @app.route('/income_bar_chart', methods=['GET', 'POST'])
    def income_bar_chart():
        try:
            bar_chart_income()
            return redirect(url_for('reports'))
        except Exception as e:
            print(f"Error {e}")            
            return redirect(url_for('reports'))

    return app
