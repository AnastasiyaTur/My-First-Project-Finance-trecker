from webapp.models import AccountType, BudgetType, СategoryName, Transaction, User


def account_transactions():
    transaction_list = Transaction.query.filter_by(budget_type_id=1).all()
    accounts = AccountType.query.filter_by().all()

    
    for transaction in transaction_list:
        for account in accounts:            
            if transaction.account_type_id == account.id:
                account.amount = account.amount - transaction.amount
                return account.amount
            


