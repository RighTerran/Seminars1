# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности
import random

# list = []
# for i in range(10):
#     list.append(random.randint(1, 10))
# print(list)
#
# list2 = []
#
# count = 0
# for i in list:
#     if list.count(i) == 1:
#         list2.append(i)
#
# print(list2)

# Сокращенный вариант
list = []
for i in range(10):
    list.append(random.randint(1, 10))
print(list)

list2 = [i for i in range(10) if list.count(i) == 1]
print(list2)
