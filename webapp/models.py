from database import Base, engine
from flask_login import UserMixin
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash


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


class BudgetType(Base):
    # Create a table with type of budget: Income and Expenses
    __tablename__ = 'budget_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    transaction = relationship("Transaction", overlaps="budget_type")
    category_name = relationship("СategoryName", overlaps="budget_type")

    def __repr__(self):
        return f'<Type of budget: {self.name}>'


class СategoryName(Base):
    # Create a table with different categories (Ex., Salary, Groceries, etc.)
    __tablename__ = 'category_name'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    budget_type_id = Column(Integer, ForeignKey(BudgetType.id),
                            index=True, nullable=False)
    transaction = relationship("Transaction", overlaps="category_name")
    budget_type = relationship("BudgetType", overlaps="category_name")

    def __repr__(self):
        return f'<Category {self.name}>'


class AccountType(Base):
    # Create a table with type of account (Ex., Cash, Visa card, Bank, etc.)
    __tablename__ = 'account_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    transaction = relationship("Transaction", overlaps="account_type")

    def __repr__(self):
        return f'<Type of account: {self.name}>'


class Transaction(Base):
    # Create a table with transactions. Sort by specific categories
    # based on budget type and account type
    # (Ex., Visa card: Clothes = -500$ (Expense), 12.09.2022)
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    amount = Column(Float)
    date_of_transaction = Column(Date)
    category_name_id = Column(Integer, ForeignKey(СategoryName.id),
                              index=True, nullable=False)
    account_type_id = Column(Integer, ForeignKey(AccountType.id),
                             index=True, nullable=False)
    budget_type_id = Column(Integer, ForeignKey(BudgetType.id),
                            index=True, nullable=False)    
    account_type = relationship("AccountType", overlaps='transaction')
    budget_type = relationship("BudgetType", overlaps='transaction')
    category_name = relationship("СategoryName", overlaps='transaction')

    def __repr__(self):
        return (f'<Transaction from {self.date_of_transaction}: '
                f'{self.account_type_id} -- {self.category_name_id} = '
                f'{self.amount}$ ({self.budget_type_id})({self.description})>')


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
