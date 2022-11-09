## **In English (below is the version in Russian)**

# Finance Tracker project

Finance Tracker is an application for keeping track of your income and expenses. With the ability to add (delete, edit) data for specific categories (For example: Salary, Gifts, Products, Communal payments, etc.) depending on the type of budget (income, expenses). And also look at the statistics of expenses and income in whole, or for a specific category. So, it is easier to plan and manage your funds.


> Implementing Table Structure in a Database with SQLAlchemy

The database management system PostgreSQL was used in the project.
- you can download and install PostgreSQL for your operating system at [link](https://www.postgresql.org/download/)
- or you can use the cloud server [ElephantSQL](https://www.elephantsql.com/)

## Installing ElephantSQL
- Account registration in the cloud:

1. Click the **Get a managed database today** button and select the Free plan
2. At the next step, click **Sign Up** and register an account
3. An email will be sent to the email address that was entered. Follow the link in the email and create a password

- Database creation

1. After registration, you need to create a database, to do this, click the **Create New Instance** button
2. Come up with a name for the instance and choose a tariff plan - free is enough (Free)
3. Select the region where the database will be located. For example, for the European part of Russia, Belarus, Lithuania, select EU-North-1 (Stockholm) or EU-West-1 (Ireland)
4. Check selection and click **Create Instance**

## Database connection
- Use the program [Valentina Studio](https://www.valentina-db.com/ru/store/category/12-valentina-studio), which works with various DBMS. It has versions for Windows, MacOS and Linux.
1. Select license type **New**, operating system, click **Add to cart** and after adding to cart - **Proceed to checkout**
2. Fill out the registration form. After successful registration, the program activation key will be sent to the email. Download Valentina Studio for the desired operating system, install and run it. When you first start it will require you to enter an activation key
3. Go to the created database page in your ElephantSQL account, and click *"Add bookmark"* in Valentina Studio. After you fill out the connection creation form in Valentina Studio, click *"Test connection"* and save the bookmark.

## Installing libraries
Create a folder for the project and a virtual environment. Then install the library for working with PostgreSQL and SQLAlchemy itself:

```
pip install psycopg2-binary
pip install sqlalchemy
```

## Create tables in the database
We connect to the database using Valentina Studio and check that the tables have appeared there.
```
python models.py
```

## Run application
In the command line, run the *"run.bat"* file (the path to the project folder is specified in cmd and the virtual environment is activated; after that we write *"run"*). We copy the address, for example, *"http://127.0.0.1:5000"* and run it in the browser. We are working on the app.


## **In Russian**

# Проект Finance Trecker

Finance Trecker - это приложение для учета своих доходов и расходов. С возможностью добавлять (удалять, редактировать) данные по конкретным категориям (Например, Зарплата, Подарки, Продукты, Коммунальные платежи и т.д.) в зависимости от типа бюджета (доход, расходы). А также смотреть статистику расходов и доходов в целои, либо по конкретной категории. Таким образом, легче планировать и управлять своими средствами.


>  Реализация структуры таблиц в базе данных с помощью SQLAlchemy

В проекте использовалась система управления базами данных (СУБД) PostgreSQL.
- скачать и установить PostgreSQL для своей операционной системы можно по [ссылке](https://www.postgresql.org/download/)
- либо можно использовать облачный сервер [ElephantSQL](https://www.elephantsql.com/)

## Установка ElephantSQL
- Регистрация аккаунта в облаке:

1. Нажать кнопку **Get a managed database today** и выбрать тарифный план Free
![](https://drive.google.com/file/d/1lOck_RK6gmLVcWUSmqzGk2aCCFBkiJXU/view?usp=sharing)
2. На следующем этапе нажать **Sign Up** и зарегистрировать аккаунт
![](https://drive.google.com/file/d/1W5MBsF_0ul8ZjWXC0nsSa1AwxTSuzL9l/view?usp=sharing)
3. На электронный адрес, который был введен, придет письмо. Перейти по ссылке из письма и придумать пароль

- Создание БД

1. После регистрации необходимо создать БД, для этого нажать кнопку **Create New Instance**
![](https://drive.google.com/file/d/1T-7j4tpvhHk26QjYXSOOd9MEO8ZvhE-g/view?usp=sharing)
2. Придумать название инстансу и выбрать тарифный план - достаточно бесплатного (Free)
3. Выбрать регион, в котором будет размещаться база данных. Например, для европейской части России, Беларуси, Литвы выбрать EU-North-1 (Stockholm) или EU-West-1 (Ireland)
4. Проверить выбор и нажать **Create Instance**

## Подключение к БД
- Использовать программу [Valentina Studio](https://www.valentina-db.com/ru/store/category/12-valentina-studio), которая работает с различными СУБД. У нее есть версии для Windows, MacOS и Linux.
![](https://drive.google.com/file/d/17Lahd0suVItgPZFmjhF_WI-k6hpkaAmb/view?usp=sharing)
1. Выбрать тип лицензии **New**, операционную систему, нажать **Add to cart** и после добавления в корзину - **Proceed to checkout**
![](https://drive.google.com/file/d/1wZ5vQsPdbkCw_PdLopRq92Xb-w6YxOZ3/view?usp=sharing)
2. Заполнить форму регистрации. После успешной регистрации на почту придет ключ активации программы. Скачать Valentina Studio для нужной операционной системы, установить и запустить ее. При первом запуске она потребует ввести ключ активации
3. В личном кабинете ElephantSQL перейти на страницу созданной базы данных, а в Valentina Studio нажать *"Добавить закладку"*. После того, как вы заполните форму создания подключения в Valentina Studio, нажать *"Проверить подключение"* и сохранить закладку.
![](https://drive.google.com/file/d/1qMK-Zqu5qDMPtEzC3m5vR6LHocZelMXy/view?usp=sharing)

## Установка библиотек
Создаем папку для проекта и виртуальное окружение. Затем устанавливаем библиотеку для работы с PostgreSQL и саму SQLAlchemy:

```
pip install psycopg2-binary
pip install sqlalchemy
```

## Создание таблиц в БД

Подключаемся к базе данных с помощью Valentina Studio и проверяем, что таблицы там появились.
```
python models.py
```

## Запуск приложения

В командной строке запускаем файл run.bat (в cmd прописан путь к папке проекта и активировано виртуальное окружение; после чего пишем run). Копируем адрес, например, http://127.0.0.1:5000 и запускаем его в браузере. Работаем в приложении.
