marks = input('Введите оценки: ').split()
marks = [int(mark) for mark in marks]


def change_marks(arr):
    max_mark = max(arr)
    min_mark = min(arr)
    for i in range(len(arr)):
        if arr[i] == max_mark:
            arr[i] = min_mark
    return arr


print('Исправленные оценки:')

print(*change_marks(marks))
