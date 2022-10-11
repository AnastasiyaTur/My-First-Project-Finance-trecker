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

1. После регистрации необходимо создаьб БД, для этого нажать кнопку **Create New Instance**
![](https://drive.google.com/file/d/1T-7j4tpvhHk26QjYXSOOd9MEO8ZvhE-g/view?usp=sharing)
2. Придумать название инстансу и выбрать тарифный план - достаточно бесплатного (Free)
3. Выбрать регион, в котором будет размещаться база данных. Например, для европейской части России, Беларуси, Литвы выбрать EU-North-1 (Stockholm) или EU-West-1 (Ireland)
4. Проверить выбор и нажать **Create Instance**

## Подключение к БД
- Использовать программу [Valentina Studio](https://www.valentina-db.com/ru/store/category/12-valentina-studio), которая работает со различными СУБД. У нее есть версии для Windows, MacOS и Linux.
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


# *файл README будет ещё редактироваться* :-)