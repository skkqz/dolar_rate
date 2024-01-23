import requests
from typing import Dict, Union


def get_course() -> Union[Dict[str, Union[str, int, float]], None]:
    """
    Получить актуальный курс рубля к доллару.
    :return: dict: Словарь с данными по курсу.
    """

    try:
        response = requests.get(url='https://www.cbr-xml-daily.ru/daily_json.js')

        return response.json()['Valute']['USD']
    except requests.exceptions.RequestException as e:
        # Логирование ошибок
        return None
