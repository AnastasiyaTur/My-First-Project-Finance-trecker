from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey

from database import Base, engine


class User(Base):
    #Сreating a table of users where personal data of users will be saved
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __repr__(self):
        return f'<User {self.username} {self.email}>'


class Сategory_name(Base):
    #Creating a table with different categories (Ex., Salary, Groceries, etc.)
    __tablename__ = 'category_name'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'<Category {self.name}>'


class Budget_type(Base):
    #Creating a table with type of budget: Income and Expenses
    __tablename__ = 'budget_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'<Type of budget: {self.name}>'


class Budget(Base):
    #Creating a table with a specific type of budget. Sort by specific categories. (Ex., Income:Salary-2000$, 10.09.2022) 
    __tablename__ = 'budget'

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    date_of_transaction = Column(Date)
    budget_type_id = Column(Integer, ForeignKey(Budget_type.id), index=True, nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), index=True, nullable=False)
    category_name_id = Column(Integer, ForeignKey(Сategory_name.id), index=True, nullable=False)

    def __repr__(self):
        return f'<{self.budget_type_id}: {self.category_id} - {self.amount}, {self.date_of_transaction}>'


class Account_type(Base):
    #Creating a table with type of account (Ex., Cash, Visa card, Bank, etc.)
    __tablename__ = 'account_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'<Type of account: {self.name}>'


class Account(Base):
    #Creating a table with a specific type of account. Sort by specific categories based on budget type 
    # (Ex., Visa card: Clothes = -500$ (Expense), 12.09.2022)
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    date_of_transaction = Column(Date)
    category_name_id = Column(Integer, ForeignKey(Сategory_name.id), index=True, nullable=False) 
    account_type_id = Column(Integer, ForeignKey(Account_type.id), index=True, nullable=False) 
    budget_type_id = Column(Integer, ForeignKey(Budget_type.id), index=True, nullable=False) 

    def __repr__(self):
        return (f'<{self.account_type_id}: {self.category_name_id} = ({self.budget_type_id}) {self.amount}$,'
                f'{self.date_of_transaction}>')

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)