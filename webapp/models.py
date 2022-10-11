from flask_login import UserMixin
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

from database import Base, engine


class User(Base, UserMixin):
    # Сreate a table of users where personal data of users will be saved
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String(100), nullable=False)
    

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password,
                                               method='pbkdf2:sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username} {self.email}>'


class СategoryName(Base):
    # Create a table with different categories (Ex., Salary, Groceries, etc.)
    __tablename__ = 'category_name'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'<Category {self.name}>'


class BudgetType(Base):
    # Create a table with type of budget: Income and Expenses
    __tablename__ = 'budget_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'<Type of budget: {self.name}>'


class Budget(Base):
    # Create a table with the type of budget and the amount on it.
    __tablename__ = 'budget'

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    budget_type_id = Column(Integer, ForeignKey(BudgetType.id),
                            index=True, nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

    def __repr__(self):
        return f'<{self.budget_type_id}: {self.amount}>'


class AccountType(Base):
    # Create a table with type of account (Ex., Cash, Visa card, Bank, etc.)
    __tablename__ = 'account_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'<Type of account: {self.name}>'


class Transaction(Base):
    # Create a table with transactions. Sort by specific categories
    # based on budget type and account type
    # (Ex., Visa card: Clothes = -500$ (Expense), 12.09.2022)
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    date_of_transaction = Column(Date)
    category_name_id = Column(Integer, ForeignKey(СategoryName.id),
                              index=True, nullable=False)
    account_type_id = Column(Integer, ForeignKey(AccountType.id),
                             index=True, nullable=False)
    budget_type_id = Column(Integer, ForeignKey(BudgetType.id),
                            index=True, nullable=False)

    def __repr__(self):
        return (f'<Transaction from {self.date_of_transaction}: '
                f'{self.account_type_id} -- {self.category_name_id} = '
                f'{self.amount}$ ({self.budget_type_id})>')


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
