# Django-ecommerce website
Интернет-магазин на Django

### Технологии:
- Django 4.0.2
- Python 3.10.4
- Docker
- HTML, CSS (Tailwind, HTMX)
- Postgresql

Проект является интеренет-магазином, предоставляющим товары.

Через админ панель можно добавлять и удалять товары и категории, а так же 
описание к ним, изображения.

Пользователи могут выбирать товары, добавлять в корзину, оформлять заказ. Реализованна регистрация и 
авторизация, профиль пользователя с возможностью просмотра заказов.


Установка:
--
```
$ git clone https://github.com/qvog/django-ecommerce.git
$ cd django-ecommerce
$ pip install -r requirements.txt
```

> Сделайте настройку собственной базы данных! 

Миграции и создание супер-пользователя.
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

> Используйте адрес: http://127.0.0.1:8000/ (Для проверки) 

## Docker установка:

1. Build containers via `docker-compose`:

    ```bash
    docker-compose build
    ```

2. Start containers:

    ```bash
    docker-compose up
    ```

3. > Используйте адрес: http://127.0.0.1:8000/ (Для проверки) 




