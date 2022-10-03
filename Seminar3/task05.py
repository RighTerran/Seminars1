# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)


n = int(input('Введите число: '))
print(Fibonacci(n))

