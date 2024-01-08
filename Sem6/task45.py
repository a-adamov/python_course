n = int(input('Введите число: '))

# for friend1 in range(n):
#     sum1 = 0
#     for div1 in range(1, int(friend1/2)):
#         if friend1 % div1 == 0:
#             sum1 += div1
#
#     sum2 = 0
#     for div2 in range(1, int(sum1/2)):
#         if sum1 % div2 == 0:
#             sum2 += div2
#
#     if sum2 == friend1 and sum2 <= n:
#             print(f'{friend1} {sum2}')

arr = []
for i in range(1, n):
    div_sum = 0
    for j in range(1, i//2+1):
        if i % j == 0:
            div_sum += j
    arr.append(tuple([i, div_sum]))

# print(arr)

for couple1 in arr:
    for couple2 in arr[arr.index(couple1):]:
        if couple2[0] == couple1[1] and couple2[1] == couple1[0] and couple2[0] != couple1[0]:
            print(f'Дружественные числа: {couple1[0]} {couple1[1]}')
