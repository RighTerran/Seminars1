# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# list = {}
# i = 1
# number = int(input('Введите число больше 1: '))
# if number >= 1:
#     while i <= number:
#         key = i
#         val = 3 * i + 1
#         list[key] = val
#         i += 1
# else:
#     print('Ошибка! Введите число больше 1')
#
# print(f'Полученный список: {list}')

# Сокращенный вариант
list1 = []
list2 = []
i = 1
number = int(input('Введите число больше 1: '))
if number >= 1:
    while i <= number:
        key = i
        list1.append(key)
        val = 3 * i + 1
        list2.append(val)
        i += 1
else:
    print('Ошибка! Введите число больше 1')

zipped_values = zip(list1,list2)
zipped_list = dict(zipped_values)
print(f'Полученный список: {zipped_list}')