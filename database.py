import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(settings.URL_ELEPHANTSQL, pool_pre_ping=True, pool_size=100)
# pool_pre_ping -- applied to eliminate OperationalError
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
