from database import db_session
from flask import Blueprint, flash, redirect, render_template, request, url_for
from webapp.transaction.forms import AddTransaction
from webapp.transaction.models import Transaction
from webapp.category.models import СategoryName
from webapp.account.models import AccountType

blueprint = Blueprint('transaction', __name__, url_prefix='/transactions')


@blueprint.route('/new_transaction')
def new_transaction():
    # Page with a form for creating a new transaction
    title = "Add new_transaction"
    transaction_form = AddTransaction()
    categories_list = СategoryName.query.filter_by().all()
    accounts_list = AccountType.query.filter_by().all()
    return render_template('transaction/transaction.html', page_title=title,
                           form=transaction_form,
                           categories_list=categories_list,
                           accounts_list=accounts_list)


@blueprint.route("/process-create-transaction", methods=['GET', 'POST'])
def process_create_transaction():
    # Process of creating a new transaction with a record in the database
    if request.method == "POST":
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
            if new_transaction.budget_type_id == 1:
                account = AccountType.query.filter_by(id=new_transaction.account_type_id).first()
                account.amount -= new_transaction.amount
                db_session.commit()
                flash('A new transaction create successfully')
                return redirect(url_for('budget.budget_expenses'))
            else:
                account = AccountType.query.filter_by(id=new_transaction.account_type_id).first()
                account.amount += new_transaction.amount
                db_session.commit()
                flash('A new transaction create successfully')
                return redirect(url_for('budget.budget_income'))
        except Exception as e:
            print(e)
        flash('An error has occurred. Data not saved')
        return redirect(url_for('transaction.new_transaction'))
