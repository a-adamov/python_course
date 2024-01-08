n = int(input('Введите длину массива: '))
list_1 = []
for i in range(n):
    list_1.append(int(input('Введите число для заполнения массива: ')))

print(list_1)

count = 0
for i in range(1, n-1):
    if list_1[i+1] < list_1[i] > list_1[i-1]:
        count += 1

print(f'Число элементов, у которых оба соседних числа меньше: {count}')