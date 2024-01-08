numbers = [int(input("Введите целое число: ")) for i in range(5)]

count = 0

for i in range(len(numbers)-1):
    if numbers[i+1] > numbers[i]:
        count += 1

print(f"Количество элементов, больше предыдущего: {count}")

