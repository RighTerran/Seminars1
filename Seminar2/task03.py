# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму
# Для n = 5: сумма = 11,55
list = []
i = 1
sum = 0
number = int(input('Введите число больше 1: '))
if number >= 1:
    while i <= number:
        value = (1 + (1 / i)) ** i
        sum = sum + value
        list.append(round(value,2))
        i += 1
else:
    print('Ошибка! Введите число больше 1')

print(f'Полученный список: {list}')
print(f'Сумма элементов списка: {round(sum, 2)}')