# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

list = []
i = 1
sum = 1
number = int(input('Введите число больше 1: '))
if number >= 1:
    while i <= number:
        sum = sum * i
        list.append(sum)
        i += 1
else:
    print('Ошибка! Введите число больше 1')

print(f'Полученный список: {list}')
