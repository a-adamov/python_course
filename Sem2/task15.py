n = int(input("Введите количество арбузов: "))
w = int(input("Введите вес арбуза: "))
min_weight = w
max_weight = w
for i in range(1, n):
    w = int(input("Введите вес арбуза: "))
    if w > max_weight:
        max_weight = w
    if w < min_weight:
        min_weight = w

print(f"Самый легкий арбуз - {min_weight} кг, самый тяжелый - {max_weight} кг")
