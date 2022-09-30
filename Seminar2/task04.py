# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

list = []
number = int(input('Введите число больше 1: '))
i = - number
if number >= 1:
    while i <= number:
        list.append(i)
        i += 1
else:
    print('Ошибка! Введите число больше 1')

print(f'Полученный список: {list}')

with open('file.txt', 'w') as data:
    data.write('1')
    data.write('2')

str = open('file.txt')
index_1 = int(str.read(1))
index_2 = int(str.read(2))
str.close()

print(f'Индексы в файле file.txt: {index_1},{index_2}')
mult = list[index_1]*list[index_2]
print(f'Произведение элементов на указанных позициях: {mult}')


