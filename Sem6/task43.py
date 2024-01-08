n = int(input('Введите длину массива: '))

arr1 = []
arr2 = []
count = 0

for i in range(n):
    k = int(input('Введите число для заполнения массива: '))
    arr1.append(k)
    if k in arr2:
        count += 1
        arr2.remove(k)
    else:
        arr2.append(k)


print(arr1)
print(f'Количестов парных элементов: {count}')

# list1 = [1, 1, 2, 3, 4, 1, 1, 2]
# count = 0
#
# for i in range(len(list1)):
#     for j in range(i+1, len(list1)):
#         if i != j and list1[i] == list1[j]:
#             count += 1
#
# print(list1)
# print(count)