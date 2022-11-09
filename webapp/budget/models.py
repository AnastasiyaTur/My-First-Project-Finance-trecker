from database import Base, engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class BudgetType(Base):
    # Create a table with type of budget: Income and Expenses
    __tablename__ = 'budget_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    transaction = relationship("Transaction", overlaps="budget_type")
    category_name = relationship("СategoryName", overlaps="budget_type")

    def __repr__(self):
        return f'<Type of budget: {self.name}>'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
