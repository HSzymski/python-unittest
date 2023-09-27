from datetime import date
import random


def get_code():
    rand_int = random.randint(0, 9)
    return f'XC-{rand_int}'


def get_today_name():
    return date.today().strftime('%a')


def get_code_with_day():
    code = get_code()
    dayname = get_today_name()

    return f'{code}-{dayname}'
