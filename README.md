# CAFE_ORDERS

Сервис для управления заказами.
### 🔥 Возможности

- Создание, редактирование, удаление, просмотр заказов.
- REST API

### Технологии

[![Django][Django-badge]][Django-url]
[![DRF][DRF-badge]][DRF-url]
[![SQLite][SQLite-badge]][SQLite-url]

## ⚙ Начало Работы

Чтобы запустить проект, следуйте инструкциям ниже.

### ⚠ Зависимости

- [Python 3.7+][Python-url]

### Установка

1. **Клонируй репозиторий**

    ```shell
    git clone https://github.com/AhmedZulkarnaev/cafe_orders
    cd YaCut
    ```

## 👀 Использование

![Usage-example](docs/usage_example.gif)

### API (Docs: [OpenAPI](docs/openapi.yml))

- **POST** `/api/orders/`
- **GET** `/api/orders/{id}/`

## 🛠 Development

1. **Создай и активируй виртуальное оркужение**

    ```shell
    python -m venv venv
    source venv/bin/activate  # (Windows: venv\Scripts\activate)
    pip install -r requirements.txt
    ```

2. **Установи зависимости проекта**

    ```shell
    pip install -r requirements.txt
    ```

3. **Запусти dev-сервер**

    ```shell
    python manage.py runserver
    ```
   
---

### ⚠️ ВНИМАНИЕ!  
Данный проект разработан в соответствии с техническим заданием (ТЗ), без учета масштабируемости и дальнейшего расширения.  

Модель `Dish` создана исключительно для удобства добавления блюд в заказ и не предполагает сложной логики управления меню.  

Все функциональные возможности реализованы в рамках поставленного ТЗ и в соответствии с его интерпретацией.  
(Возможно, некоторые моменты могли быть для меня не вполне ясны.) 