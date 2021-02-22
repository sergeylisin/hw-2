"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

FILE_NAME = 'referat.txt'
FILE_NAME2 = 'referat2.txt'

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open(FILE_NAME,'r') as referat_file:
        referat_str = referat_file.read()
        print("length = {}".format(len(referat_str)))
        print("words = {}".format(len(referat_str.split())))
        str2 = referat_str.replace('.','!')
    with open(FILE_NAME2,'w') as referat_file2:
        referat_file.write(str2)

if __name__ == "__main__":
    main()
