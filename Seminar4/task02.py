# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

n = int(input('Введите натуральное число: '))
p = 2
list = []
a = n
while (a > 1):
    if n % p == 0:
        list.append(p)
        n = n / p
        if n == 1:
            break
    else:
        p += 1
print(list)
