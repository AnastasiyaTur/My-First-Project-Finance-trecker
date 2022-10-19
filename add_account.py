from database import db_session
from webapp.models import AccountType

default_account_type1 = AccountType(name='Cash')
db_session.add(default_account_type1)
db_session.commit()

default_account_type2 = AccountType(name='Card MasterCard')
db_session.add(default_account_type2)
db_session.commit()

default_account_type3 = AccountType(name='Bank')
db_session.add(default_account_type3)
db_session.commit()
