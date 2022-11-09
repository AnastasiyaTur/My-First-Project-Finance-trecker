from database import Base, engine
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship


class AccountType(Base):
    # Create a table with type of account (Ex., Cash, Visa card, Bank, etc.)
    __tablename__ = 'account_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    transaction = relationship("Transaction", overlaps="account_type")

    def __repr__(self):
        return f'<Type of account: {self.name}>'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
