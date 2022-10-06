#Здесь я создавала админа (по урокам в видео), чтобы проверить создается ли пользователь

from getpass import getpass
import sys

from database import Base, engine
from webapp import create_app
from webapp.models import User

app = create_app()

with app.app_context():
    username = input('Enter your name:')
    
    if User.query.filter(User.username == username).count():
        print('A user with the same name already exists')
        sys.exit(0)

    password1 = getpass('Enter your password')
    password2 = getpass('Repeat password')

    if not password1 == password2:
        print('Passwords do not match')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    #db.session.add(new_user)  закомментировала пока, так понимаю, что с базой данных не связана пока
    #db.session.commit()
    