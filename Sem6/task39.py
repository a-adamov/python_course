n = int(input('Введите длину первого массива: '))
list_1 = []
for i in range(n):
    list_1.append(int(input('Введите число для заполнения массива: ')))

list_2 = []
m = int(input('Введите длину второго массива: '))
for i in range(m):
    list_2.append(int(input('Введите число для заполнения массива: ')))

print(list_1)
print(list_2)

res = []
for i in list_1:
    if i not in list_2:
        res.append(i)

print(f'Элементы первого массива, которых нет во втором: {res}')