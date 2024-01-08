n = int(input("Введите целое число: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print(f"Факториал числа равен {fact}")