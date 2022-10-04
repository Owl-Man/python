# 79000000000

phone_book = {}


def normalize_phone_number(number):
    number = number.replace(' ', '').replace('-', '')

    if number[:2] == '+7' and len(number) == 12:
        return number
    if number[0] == '8' and len(number) == 11:
        number = number.replace('8', '+7', 1)
        return number
    if number[0] == '9' and len(number) == 10:
        number = '+7' + number
        return number

    return '0'


def normalize_name(name):
    name.lower()

    name_surname = name.split(' ')
    name_surname[0] = name_surname[0].capitalize()
    name_surname[1] = name_surname[1].capitalize()

    name = name_surname[0] + ' ' + name_surname[1]

    return name


def add_contact(name, number):
    if normalize_phone_number(number) != '0':
        number = normalize_phone_number(number)
        name = normalize_name(name)

        print(number, name)

        phone_book[name] = number
        print('Добавлено')
    else:
        print('Неправильно набран номер')


def remove_contact(name):
    name = normalize_name(name)
    phone_book.pop(name, 'Такого контакта в книге нет')

    print('Удалено')


def change_contact(name, number):
    name = normalize_name(name)
    if name in phone_book:
        phone_book[name] = number
    else:
        print('Такого контакта в книге нет')


while True:
    command = int(input())

    if command == 1:
        name = input('Введите имя и фамилию \n')
        number = input('Введите номер \n')
        add_contact(name, number)
    elif command == 2:
        name = input('Введите имя и фамилию \n')
        remove_contact(name)
    elif command == 3:
        print(phone_book)
    elif command == 4:
        name = input('Введите имя и фамилию \n')
        number = input('Введите новый номер \n')
        change_contact(name, number)
    elif command == 5:
        break
    else:
        print('Неверная команда')