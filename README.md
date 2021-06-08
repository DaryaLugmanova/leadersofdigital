# leadersofdigital

## Установка / Использование 
### Скачайте и установите зависимости
Выполните в консоли:
```
https://github.com/DaryaLugmanova/leadersofdigital.git
cd leadersofdigital
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

### Выполните настройку
Переименуйте файл env.example в .env и замените  следующие данные:
```
DJANGO_SECRET_KEY = DJANGO_SECRET_KEY

DB_NAME = Название базы данных
DB_USER = Пользователь базы данных
DB_PASSWORD = Пароль базы данных
DB_HOST = Хост базы данных
DB_PORT = Порт базы данных
```
### Наполните базу данных и создайте админа
```
python manage.py migrate
python manage.py createsuperuser
```

### Запустите сервер
```
python3 manage.py runserver
```
### Перейдите на [локальный сервер](http://127.0.0.1:8000)

## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)