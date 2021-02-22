import csv

"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

NAMES = [
    {'name':'John', 'age':31 , 'job':'job1'},
    {'name':'Иван', 'age':32 , 'job':'job2'},
    {'name':'Jack', 'age':33 , 'job':'job3'},
    {'name':'Яков', 'age':34 , 'job':'job4'},
    {'name':'Peter', 'age':35 , 'job':'job5'},
    {'name':'Пётр', 'age':31 , 'job':'job6'},
    {'name':'Basil', 'age':32 , 'job':'job7'},
    {'name':'Василий', 'age':33 , 'job':'job8'},
    {'name':'George', 'age':34 , 'job':'job9'},
    {'name':'Юрий', 'age':35 , 'job':'job0'}
]

CSV_FILE_NAME='out.csv'

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open(CSV_FILE_NAME,'w') as csv_file:
        writer = csv.DictWriter(csv_file,['name','age','job'])
        writer.writerows(NAMES)

if __name__ == "__main__":
    main()
