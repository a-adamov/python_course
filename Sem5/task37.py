number = int(input('Введите длину последовательности: '))


def spin_line(n):
    if n == 0:
        return ''
    k = int(input('Введите число: '))
    return spin_line(n-1) + str(k)


print(f'Обратная последовательность: {spin_line(number)}')
