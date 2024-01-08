numbers = [int(input("Введите целое число: ")) for i in range(8)]

# count = 0
# used_numbers = list()
# for number in numbers:
#     if number not in used_numbers:
#         used_numbers.append(number)
#         count += 1

# Способ через преобразование списка в множество
print(f"Количество используемых чисел: {len(set(numbers))}")