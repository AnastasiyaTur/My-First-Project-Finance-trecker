from database import Base, engine
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
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


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
