n = int(input("Введите натуральное число: "))
f0 = 1
f = 2
i = 3
while f < n:
    f += f0
    f0 = f - f0
    i += 1

if f == n:
    print(f"Число Фибоначчи под номером {i}")
else:
    print(f"Не является числом Фибоначчи")