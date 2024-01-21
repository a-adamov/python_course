# импортируем функции
from data_create import name_data, surname_data, phone_data, address_data, rec_data


def input_data():
    # определяем количество записей и получаем данные
    rec_number = rec_data()
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    # определяем вариант записи
    variant = int(input(f'В каком формате записать данные? \n\n'
                        f'вариант 1:\n\n'
                        f'{name}\n{surname}\n{phone}\n{address}\n\n'
                        f'вариант 2:\n\n'
                        f'{name};{surname};{phone};{address}\n\n'
                        f'Выберите вариант: '
                        ))
    # проверяем правильность ввода варианта
    while variant != 1 and variant != 2:
        print('Неправильный ввод')
        variant = int(input('Введите число: '))
    #записываем новые данные, изменяя количество записей
    if variant == 1:
        with open('data1.csv', 'r', encoding='utf-8') as file:
            old_data = file.read()
        new_data = old_data.replace(f'Записей: {rec_number[0]}', f'Записей: {rec_number[0] + 1}')
        with open('data1.csv', 'w', encoding='utf-8') as file:
            file.write(new_data)
        with open('data1.csv', 'a', encoding='utf-8') as file:
            file.write(f'Запись {rec_number[0] + 1}:\n{name}\n{surname}\n{phone}\n{address}\n\n')
    elif variant == 2:
        with open('data2.csv', 'r', encoding='utf-8') as file:
            old_data = file.read()
        new_data = old_data.replace(f'Записей: {rec_number[1]}', f'Записей: {rec_number[1] + 1}')
        with open('data2.csv', 'w', encoding='utf-8') as file:
            file.write(new_data)
        with open('data2.csv', 'a', encoding='utf-8') as file:
            file.write(f'Запись {rec_number[1] + 1}: {name};{surname};{phone};{address}\n\n')


def print_data():
    # выводим данные
    print('Вывожу данные из файла 1: \n\n')
    with open('data1.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))
    print('Вывожу данные из файла 2: \n\n')
    with open('data2.csv', 'r', encoding='utf-8') as file:
        data_second = file.readlines()
        print(*data_second)

def change_data():
    # определяем количество записей
    rec_number = rec_data()
    # определяем файл для изменений
    variant = int(input(f'В каком файле изменить запись (1 или 2)?: '))
    # проверяем правильность ввода варианта
    while variant != 1 and variant != 2:
        print('Неправильный ввод')
        variant = int(input('Введите число: '))

    if variant == 1:
        changed_rec = int(input('Введите номер изменяемой записи: '))
        # проверяем правильность ввода номера записи
        while changed_rec not in range(1, rec_number[0] + 1):
            print('Такой записи не существует')
            changed_rec = int(input('Введите номер изменяемой записи: '))
        # получаем новые данные
        print('Введите новые данные: ')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        # читаем и перезаписываем данные до и после изменяемой записи, в промежутке вставляем измененные данные
        with open('data1.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            changed_line_index = data_first.index(f'Запись {changed_rec}:\n')
            data_first_top = data_first[:changed_line_index + 1]
            data_first_bottom = data_first[changed_line_index + 5:]

        with open('data1.csv', 'w', encoding='utf-8') as file:
            for line in data_first_top:
                file.write(line)
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n')
            for line in data_first_bottom:
                file.write(line)

    elif variant == 2:
        changed_rec = int(input('Введите номер изменяемой записи: '))

        while changed_rec not in range(1, rec_number[1] + 1):
            print('Такой записи не существует')
            changed_rec = int(input('Введите номер изменяемой записи: '))

        print('Введите новые данные: ')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()

        with open('data2.csv', 'r', encoding='utf-8') as file:
            data_second = file.readlines()
            for line in data_second:
                if f'Запись {changed_rec}:' in line:
                    changed_line_index = data_second.index(line)
            data_second_top = data_second[:changed_line_index]
            data_second_bottom = data_second[changed_line_index + 2:]

        with open('data2.csv', 'w', encoding='utf-8') as file:
            for line in data_second_top:
                file.write(line)
            file.write(f'Запись {changed_rec}: {name};{surname};{phone};{address}\n\n')
            for line in data_second_bottom:
                file.write(line)

def delete_data():
    # определяем количество записей
    rec_number = rec_data()
    # определяем файл для изменения
    variant = int(input(f'В каком файле удалить запись (1 или 2)?: '))
    # проверяем правильность ввода файла
    while variant != 1 and variant != 2:
        print('Неправильный ввод')
        variant = int(input('Введите число: '))
    # читаем и записываем в файл данные до и после удаляемой записи, меняя кол-во и порядковые номера записей
    if variant == 1:
        del_rec = int(input('Введите номер удаляемой записи: '))

        while del_rec not in range(1, rec_number[0] + 1):
            print('Такой записи не существует')
            del_rec = int(input('Введите номер удаляемой записи: '))

        with open('data1.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            del_line_index = data_first.index(f'Запись {del_rec}:\n')
            data_first_top = data_first[1:del_line_index]
            data_first_bottom = data_first[del_line_index + 6:]

        with open('data1.csv', 'w', encoding='utf-8') as file:
            file.write(f'Записей: {rec_number[0] - 1}\n')
            for line in data_first_top:
                file.write(line)
            current_rec = del_rec + 1
            for line in data_first_bottom:
                if f'Запись {current_rec}:' in line:
                    file.write(f'Запись {current_rec - 1}:\n')
                    current_rec += 1
                else:
                    file.write(line)

    elif variant == 2:
        del_rec = int(input('Введите номер удаляемой записи: '))

        while del_rec not in range(1, rec_number[1] + 1):
            print('Такой записи не существует')
            del_rec = int(input('Введите номер удаляемой записи: '))

        with open('data2.csv', 'r', encoding='utf-8') as file:
            data_second = file.readlines()
            for line in data_second:
                if f'Запись {del_rec}:' in line:
                    del_line_index = data_second.index(line)
            data_second_top = data_second[1:del_line_index]
            data_second_bottom = data_second[del_line_index + 2:]

        with open('data2.csv', 'w', encoding='utf-8') as file:
            file.write(f'Записей: {rec_number[0] - 1}\n')
            for line in data_second_top:
                file.write(line)
            current_rec = del_rec + 1
            for line in data_second_bottom:
                if line != '\n':
                    file.write(f'Запись {current_rec - 1}: ' + line[9 + len(str(current_rec-1)):])
                    current_rec += 1
                else:
                    file.write(line)