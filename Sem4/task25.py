# string = (input("Введите символы через пробел: ")).split()
#
# new_string = []
#
# for char in string:
#     count = 0
#     for new_char in new_string:
#         if new_char[0] == char:
#             count += 1
#     if count > 0:
#         new_string.append(char + '_' + str(count))
#     else:
#         new_string.append(char)
#
# new_string = " ".join(new_string)
#
# print(f"Новая строка: {new_string}")

string = (input("Введите символы через пробел: ")).split()

res = {}

for char in string:
    if char in res:
        print(f"{char}_{res[char]}", end=' ')
    else:
        print(char, end=' ')
    res[char] = res.get(char, 0) + 1


