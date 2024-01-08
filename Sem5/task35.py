number = int(input('Введите число: '))


def check_simple(n):
    flag = True
    i = 2
    while i < int(n/2) and flag:
        if n % i == 0:
            flag = False
        i += 1
    return 'Число простое' if flag else 'Число составное'


print(check_simple(number))
