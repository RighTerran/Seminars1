# Напишите программу, которая будет преобразовывать десятичное число в двоичное

digit = int(input('Введите число: '))
list = []
while (digit >= 1):
    if digit != 1:
        n = digit % 2
        digit = digit // 2
        list.append(n)
    else:
        list.append(digit) # добавляем последнее число
        break

list.reverse() # переворачиваем список
str = "".join(str(i) for i in list) # преобразуем в строку
print(f'Двоичное представление: {str}')
