


from csv import DictReader, DictWriter
from os.path import exists

file_name = 'phone.csv'


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    first_name = 'Ivan'
    last_name = 'Ivanov'
    phone_number = None

    is_valid = False
    while not is_valid:
        try:
            phone_number = 99988811123
            # phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                raise LenNumberError('Неверная длина номера')
            else:
                is_valid = True
        except ValueError:
            print('Невалидный номер')
        except LenNumberError as err:
            print(err)
            continue

    info = [first_name, last_name, phone_number]

    return info

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def write_file(lst):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)

    values = [el['Телефон'] for el in res]

    if str(lst[2]) in values:
        print('Такой номер уже существует')
        return

    obj = {'Имя':  lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}

    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        res.append(obj)
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def copy_file(file_name):
    number_line = int(input('Введите номер строки для копирования (начиная с 1): '))
    with open(file_name, 'r', encoding='utf-8') as firstfile:
        f_reader = firstfile.readlines()
        f_read = f_reader[number_line - 1]
    with open('backup.csv', 'w+', encoding='utf-8') as secondfile:
        secondfile.write(str(f_read))


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл не создан')
                continue
            print(*read_file(file_name))
        elif command == 'c':
            copy_file(file_name)
main()
