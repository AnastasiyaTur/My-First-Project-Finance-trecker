from database import Base, engine
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from webapp.account.models import AccountType
from webapp.budget.models import BudgetType
from webapp.category.models import СategoryName


class Transaction(Base):
    # Create a table with transactions. Sort by specific categories
    # based on budget type and account type
    # (Ex., Visa card: Clothes = 500$ (Expense), 12.09.2022)
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
