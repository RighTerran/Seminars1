# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]
list2 = []
print(f'Список: {list}')

if len(list) % 2 == 0:
    for i in range(int(len(list) / 2)):
        mult = list[i] * (list[len(list) - 1] - i)
        list2.append(mult)
else:
    for i in range(int((len(list) / 2)) + 1):
        list2.append(list[i] * (list[len(list) - 1] - i))

print(f'Новый список произведений пар чисел списка: {list2}')
