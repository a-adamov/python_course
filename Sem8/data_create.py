def name_data():
    name = input('Введите имя: ')
    return name

def surname_data():
    surname = input('Введите фамилию: ')
    return surname

def phone_data():
    phone = input('Введите номер телефона: ')
    return phone

def address_data():
    address = input('Введите адрес: ')
    return address

def rec_data():
    with open('data1.csv', 'r', encoding='utf-8') as file:
        line1 = file.readline()
        rec_number1 = int(line1.split()[1])
    with open('data2.csv', 'r', encoding='utf-8') as file:
        line1 = file.readline()
        rec_number2 = int(line1.split()[1])
    rec_number = [rec_number1, rec_number2]
    return rec_number