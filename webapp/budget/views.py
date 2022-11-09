from database import db_session
from flask import Blueprint, flash, redirect, render_template, request, url_for
from webapp.transaction.models import Transaction
from webapp.category.models import СategoryName
from webapp.account.models import AccountType

blueprint = Blueprint('budget', __name__, url_prefix='/budget')


@blueprint.route('/budget_expenses')
def budget_expenses():
    # Page with all expenses transaction
    categories_expenses_list = СategoryName.query.order_by(СategoryName.name).filter_by(budget_type_id=1).all()
    transaction_list = Transaction.query.order_by(Transaction.date_of_transaction.desc()).filter_by().all()
    total_amount = 0
    for category in categories_expenses_list:
        for transaction in transaction_list:
            if category.id == transaction.category_name_id:
                total_amount += transaction.amount

    return render_template(
        'budget/budget_expenses.html',
        categories_expenses_list=categories_expenses_list,
        transaction_list=transaction_list,
        total_amount=total_amount)


@blueprint.route('/budget_income')
def budget_income():
    # Page with all income transaction
    categories_income_list = СategoryName.query.order_by(СategoryName.name).filter_by(budget_type_id=2).all()
    transaction_list = Transaction.query.order_by(Transaction.date_of_transaction.desc()).filter_by().all()
    total_amount = 0
    for category in categories_income_list:
        for transaction in transaction_list:
            if category.id == transaction.category_name_id:
                total_amount += transaction.amount

    return render_template(
        'budget/budget_income.html',
        categories_income_list=categories_income_list,
        transaction_list=transaction_list,
        total_amount=total_amount)


@blueprint.route('/budget/<int:id>/edit', methods=['GET', 'POST'])
def budget_edit(id):
    # Page for changing data budget
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
                return redirect(url_for('budget.budget_expenses'))
            except Exception as e:
                print(f'Error {e}')
        else:
            try:
                db_session.commit()
                return redirect(url_for('budget.budget_income'))
            except Exception as e:
                print(f'Error {e}')
    else:
        return render_template("budget/edit_budget.html",
                               transaction=transaction)


@blueprint.route('/budget/<int:id>/delete', methods=['GET', 'POST'])
def budget_delete(id):
    # Page for deleting data budget
    transaction = Transaction.query.filter_by(id=id).first()
    try:
        db_session.delete(transaction)
        db_session.commit()
        if transaction.budget_type_id == 1:
            account = AccountType.query.filter_by(id=transaction.account_type_id).first()
            account.amount += transaction.amount
            db_session.commit()
        else:
            account = AccountType.query.filter_by(id=transaction.account_type_id).first()
            account.amount -= transaction.amount
            db_session.commit()

        flash('Delete transaction successfully')
        return redirect(url_for('budget.budget_expenses'))
    except Exception as e:
        print(f'Error {e}')
        flash('An error has occurred. The account has not been removed.')
        return redirect(url_for('budget.budget_expenses'))
