import matplotlib.pyplot as plt

from webapp.transaction.models import Transaction


def pie_chart_expenses():
    # Create a pie chart for all expenses
    transaction_list = Transaction.query.filter_by(budget_type_id=1).all()
    categories = {}
    for transaction in transaction_list:
        if transaction.category_name.name in categories:
            categories[transaction.category_name.name] += transaction.amount
        else:
            categories[transaction.category_name.name] = transaction.amount

    plt.pie(categories.values(), labels=categories.keys(),
            autopct='%.2f%%', shadow=True)
    plt.title('Expense Report by Category')
    plt.legend(title="Categories",
               fontsize="x-small",
               title_fontsize="small",
               loc="lower left",
               bbox_to_anchor=(-0.3, 0.1))
    plt.show()


def pie_chart_income():
    # Create a pie chart for all income
    transaction_list = Transaction.query.filter_by(budget_type_id=2).all()
    categories = {}
    for transaction in transaction_list:
        if transaction.category_name.name in categories:
            categories[transaction.category_name.name] += transaction.amount
        else:
            categories[transaction.category_name.name] = transaction.amount

    plt.pie(categories.values(), labels=categories.keys(),
            autopct='%.2f%%', shadow=True)
    plt.title('Income Report by Category')
    plt.legend(title="Categories",
               fontsize="x-small",
               title_fontsize="small",
               loc="lower left",
               bbox_to_anchor=(-0.3, 0.1))
    plt.show()


def bar_chart_expenses():
    # Create a bar chart for all expenses
    transaction_list = Transaction.query.filter_by(budget_type_id=1).all()
    categories = {}
    for transaction in transaction_list:
        if transaction.category_name.name in categories:
            categories[transaction.category_name.name] += transaction.amount
        else:
            categories[transaction.category_name.name] = transaction.amount

    fig, ax = plt.subplots()
    category = categories.keys()
    amount = categories.values()
    ax.bar(category, amount)
    ax.set_ylabel('amount, €')
    ax.set_title('Expense Report by Category')
    ax.legend(title="Categories")
    plt.show()


def bar_chart_income():
    # Create a bar chart for all income
    transaction_list = Transaction.query.filter_by(budget_type_id=2).all()
    categories = {}
    for transaction in transaction_list:
        if transaction.category_name.name in categories:
            categories[transaction.category_name.name] += transaction.amount
        else:
            categories[transaction.category_name.name] = transaction.amount

    fig, ax = plt.subplots()
    category = categories.keys()
    amount = categories.values()
    ax.bar(category, amount)
    ax.set_ylabel('amount, €')
    ax.set_title('Income Report by Category')
    ax.legend(title="Categories")
    plt.show()
