# exchange\_app

Django-приложение для размещения объявлений и обмена между пользователями.

## Функциональность

* Регистрация и авторизация пользователей
* Создание, редактирование и удаление объявлений
* API для управления объявлениями
* Система предложений на обмен между пользователями
* Административный интерфейс
* Простая архитектура на основе Django

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/BuryatisLesa/exchange_app.git
cd exchange_app
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
venv\Scripts\activate  # Для Windows
# или
source venv/bin/activate  # Для Linux/macOS
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Выполните миграции и создайте суперпользователя:

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Запустите сервер разработки:

```bash
python manage.py runserver
```

## Тестирование

Для запуска тестов используйте:

```bash
pytest
```

## Структура проекта

```
exchange_app/
├── ads/                  # Приложение с объявлениями
├── core/                 # Конфигурация проекта
├── manage.py             # Управление проектом
├── requirements.txt      # Зависимости
└── pytest.ini            # Конфигурация pytest
```

## Контакты

Автор: Konstantin Sandanov
Репозиторий: [https://github.com/BuryatisLesa/exchange\_app](https://github.com/BuryatisLesa/exchange_app)

Почта: [kostyansandanov@gmail.com](mailto:kostyansandanov@gmail.com)
