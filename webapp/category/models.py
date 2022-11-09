from database import Base, engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from webapp.budget.models import BudgetType


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


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
