from dataclasses import dataclass


@dataclass
class ButtonText:
    START = ['Начать', 'Start']
    DAY: str = 'День'
    WEEK: str = 'Неделя'
    MONTH: str = 'Месяц'


@dataclass
class MessageText:
    FIRST_NAME: str = None
    ERROR: str = 'Я могу принимать только текстовые сообщения. Напиши город в котором хочешь узнать погоду.'
    DEFAULT: str = 'Я не знаю такого города. Попробуй другой!'
    CITY: str = None
    TEST_MAIL: str = 'Тестовая рассылка'

    def start_text(self):
        return f'Привет, {self.FIRST_NAME}, я Бот Погоды! Напиши название города в котором ты бы хотел узнать погоду?'

    def period_text(self):
        return f'На какой период вы бы хотели узнать прогноз для города - {self.CITY}?'


@dataclass
class Callback:
    TYPES = ['']

cities = ['Москва', 'Санкт-Петербург']
