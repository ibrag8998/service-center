# Как запустить?

Необходим уже установленный python версии 3.8.
Далее по инструкции.

```shell
python -m venv venv  # создание виртуального окружения
. venv/bin/activate  # активация его
pip install -r requirements.txt  # установка зависимостей
cd app  # переход в папку с кодом программы
python manage.py runserver  # запуск локального сервера
```

Далее в браузере по адресу http://localhost:8000/admin попадаем в панель администратора.
