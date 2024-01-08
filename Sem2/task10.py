coins = [0, 1, 0, 1, 0, 0]

# Введите ваше решение ниже
count = 0
heads = 0
for i in coins:
    heads += i
    count += 1

tails = count - heads
if heads > tails:
    print(tails)
else:
    print(heads)