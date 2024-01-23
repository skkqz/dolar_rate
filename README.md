# Документация для приложения "Курс Доллара к Рублю"

Это приложение предоставляет API для получения актуального курса доллара к рублю. Основной функционал включает запрос текущего курса, а также вывод списка последних 10 запросов.

## Подготовка к запуску
### Клонирование репозитория
~~~
git clone https://github.com/your-username/your-repository.git
cd dolar_rate
~~~
### Создание виртуального окружения

~~~
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate  # для Windows
~~~
### Установка зависимостей
~~~
pip install -r requirements.txt
~~~

### Запуск сервера
~~~
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
~~~

## Использование API
### Получение текущего курса
#### Request
~~~
GET /get-current-usd/

http://localhost:8000/get-current-usd/
~~~
#### Response
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "topical": 87.9199,
    "last_10_rates": [
        {
            "currency": "USD",
            "rate": 87.9199,
            "timestamp": "2024-01-23T17:12:23.459591Z"
        },
        {
            "currency": "USD",
            "rate": 87.9199,
            "timestamp": "2024-01-23T17:12:33.989811Z"
        },
        {
            "currency": "USD",
            "rate": 87.9199,
            "timestamp": "2024-01-23T17:13:00.493641Z"
        },
        {
            "currency": "USD",
            "rate": 87.9199,
            "timestamp": "2024-01-23T18:07:34.731332Z"
        },
        {
            "currency": "USD",
            "rate": 87.9199,
            "timestamp": "2024-01-23T18:11:18.976558Z"
        },
        {
            "currency": "USD",
            "rate": 87.9199,
            "timestamp": "2024-01-23T18:11:30.044114Z"
        }
    ]
}
~~~

### Ограничение частоты запросов
* Если прошло менее 10 секунд с момента последнего запроса, API вернет ошибку с кодом 429.

#### Request (слишком частые запросы)
~~~
HTTP 429 Too Many Requests
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "error": "Too many requests. Please try again later."
}
~~~

### Ошибки при получении курса
* В случае ошибки при запросе курса, API вернет соответствующее сообщение.

#### Request (ошибка при запросе)
~~~
HTTP 429 Too Many Requests
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "error": "Failed to retrieve USD to RUB rate"
}
~~~

### Участие в проекте
#### Если у вас есть предложения или исправления, создавайте issues или отправляйте pull requests. Будем рады вашему вкладу!

### Участники проекта
* [skkqz](https://github.com/skkqz/)
* 