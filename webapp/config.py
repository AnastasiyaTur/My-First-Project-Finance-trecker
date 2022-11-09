import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


DATABASE_URL = 'postgres://ekobzqae:FgJaotKRKKf58FpxifrtYsrXoRVI51rP@mouse.db.elephantsql.com/ekobzqae'
SQLALCHEMY_DATABASE_URI = os.environ.get(DATABASE_URL)


SECRET_KEY = "rjehgber56wehbf%EKRMG35%KJNGSR746%JNG"

REMEMBER_COOKIE_DURATION = timedelta(days=7)
