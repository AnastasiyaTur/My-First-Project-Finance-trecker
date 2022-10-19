# Здесь я создавала админа (по урокам в видео), чтобы проверить создается ли
# пользователь (из командной строки создавала)

import sys
from getpass import getpass

from database import db_session
from webapp import create_app
from webapp.models import User

app = create_app()

with app.app_context():
    username = input('Enter your name:')
    email = input('Enter your email:')
    if User.query.filter(User.email == email).count():
        print('A user with the same email already exists')
        sys.exit(0)

    password1 = getpass('Enter your password')
    password2 = getpass('Repeat password')

    if not password1 == password2:
        print('Passwords do not match')
        sys.exit(0)

    new_user = User(username=username, email=email)
    new_user.set_password(password1)

    db_session.add(new_user)
    db_session.commit()
