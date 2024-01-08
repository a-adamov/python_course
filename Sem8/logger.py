from data_create import name_data, surname_data, phone_data, address_data


def input_data():
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
        with open('data1.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    elif variant == 2:
        with open('data2.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')



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