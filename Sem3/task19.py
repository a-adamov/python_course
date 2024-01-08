numbers = [int(input("Введите целое число для списка: ")) for i in range(5)]
k = int(input("Введите целое число сдвига: "))
k = k % len(numbers)
for i in range(k):
    numbers.insert(0, numbers[-1])
    numbers.pop(len(numbers)-1)
print(numbers)