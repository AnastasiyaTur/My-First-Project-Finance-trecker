from database import db_session
from flask import Blueprint, flash, redirect, render_template, request, url_for
from webapp.account.forms import CreateAccount
from webapp.account.models import AccountType

blueprint = Blueprint('account', __name__, url_prefix='/accounts')


@blueprint.route('/')
def accounts():
    # Page with all created accounts and total amount.
    title = "Accounts"
    accounts_list = AccountType.query.filter_by().all()
    total_amount = 0
    for account in accounts_list:
        total_amount += account.amount
    return render_template('account/account_page.html',
                           page_title=title,
                           accounts_list=accounts_list,
                           total_amount=total_amount)


@blueprint.route('/create_account')
def create_account():
    # Page with a form for creating a new account
    title = "Create account"
    create_account_form = CreateAccount()
    return render_template('account/create_account.html', page_title=title,
                           form=create_account_form)


@blueprint.route("/process_create_account", methods=['GET', 'POST'])
def process_create_account():
    # The process of creating a new account with a record in the database
    form = CreateAccount()

    if form.validate_on_submit():
        account = AccountType.query.filter(AccountType.name == form.account_name.data).first()
        print(account)
        if account is None:
            account = AccountType(name=form.account_name.data, amount=form.amount.data)
            db_session.add(account)
            db_session.commit()
            flash('Create account successfully')
            return redirect(url_for('account.accounts'))
    flash('An error has occurred. Data not saved')
    return redirect(url_for('account.create_account'))


@blueprint.route('/account/<int:id>/edit', methods=['GET', 'POST'])
def account_edit(id):
    # Page for changing account data
    account = AccountType.query.get(id)
    if request.method == "POST":
        account.name = request.form['name']
        account.amount = request.form['amount']
        try:
            db_session.commit()
            return redirect(url_for('account.accounts'))
        except Exception as e:
            print(f'Error {e}')
    else:
        return render_template("account/edit_account.html", account=account)


@blueprint.route('/account/<int:id>/delete', methods=['GET', 'POST'])
def account_delete(id):
    # Page for deleting account data
    account = AccountType.query.filter_by(id=id).first()
    try:
        db_session.delete(account)
        db_session.commit()
        flash('Delete account successfully')
        return redirect(url_for('account.accounts'))
    except Exception as e:
        print(f'Error {e}')
        flash('An error has occurred. The account has not been removed.')
        return redirect(url_for('account.accounts'))
