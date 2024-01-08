# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

n = int(input("Введите количество чисел в списке: "))
numbers = [int(input("Введите целое число для списка: ")) for i in range(n)]
k = int(input("Введите целое число для поиска: "))

count = 0

for number in numbers:
    if number == k:
        count += 1

print(f"Число {k} встречается в списке {count} раз")