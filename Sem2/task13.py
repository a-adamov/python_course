n = int(input("Введите количество дней: "))
i = 0
length = 0
max_length = 0
while i < n:
    t = int(input("Введите температуру: "))
    if t > 0:
        length += 1
        if length > max_length:
            max_length = length
    else:
        length = 0
    i += 1

print(f"Самая длинная оттепель составила {max_length} дней")
