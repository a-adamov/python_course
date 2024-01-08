n = int(input('Введите порядковый номер числа Фибоначчи: '))
def fib(n):
    if n in [0, 1]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(f'Число Фибоначчи: {fib(n-2) if n>1 else 0}')

