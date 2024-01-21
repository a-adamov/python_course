from data_create import name_data, surname_data, phone_data, address_data, rec_data


def input_data():
    rec_number = rec_data()
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    variant = int(input(f'В каком формате записать данные? \n\n'
                        f'вариант 1:\n\n'
                        f'{name}\n{surname}\n{phone}\n{address}\n\n'
                        f'вариант 2:\n\n'
                        f'{name};{surname};{phone};{address}\n\n'
                        f'Выберите вариант: '
                        ))
    while variant != 1 and variant != 2:
        print('Неправильный ввод')
        variant = int(input('Введите число: '))

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
    rec_number = rec_data()

    variant = int(input(f'В каком файле изменить запись (1 или 2)?: '))

    while variant != 1 and variant != 2:
        print('Неправильный ввод')
        variant = int(input('Введите число: '))

    if variant == 1:
        changed_rec = int(input('Введите номер изменяемой записи: '))

        while changed_rec not in range(1, rec_number[0] + 1):
            print('Такой записи не существует')
            changed_rec = int(input('Введите номер изменяемой записи: '))

        print('Введите новые данные: ')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()

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
            # changed_line_index = data_second.index(f'Запись {changed_rec}:')
            data_second_top = data_second[:changed_line_index]
            data_second_bottom = data_second[changed_line_index + 2:]

        with open('data2.csv', 'w', encoding='utf-8') as file:
            for line in data_second_top:
                file.write(line)
            file.write(f'Запись {changed_rec}: {name};{surname};{phone};{address}\n\n')
            for line in data_second_bottom:
                file.write(line)