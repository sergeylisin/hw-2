import datetime
from datetime import datetime as dt
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = datetime.date.today()
    print((today - datetime.timedelta(days = 1)).strftime('%Y.%m.%d'))
    print(today.strftime('%Y.%m.%d'))
    print((today - datetime.timedelta(days = 30)).strftime('%Y.%m.%d'))



def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date = dt.strptime(date_string,'%d/%m/%y %H:%M:%S.%f')
    return date

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
