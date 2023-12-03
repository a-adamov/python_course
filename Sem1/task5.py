n = 385916

# Введите ваше решение ниже

first_sum = 0
sec_sum = 0

while n > 999:
    sec_sum += n % 10
    n = n//10

while n > 0:
    first_sum += n % 10
    n = n//10

if first_sum == sec_sum:
    print("yes")
else:
    print("no")