# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

# list = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(len(list)):
#     if i % 2 != 0:
#         sum += list[i]
#
# print(f'Список: {list}')
# print(f'Сумма элементов списка на нечётных позициях: {sum}')

# def getSumOdds(aList):
#     return sum(aList[i] for i in range(1,len(aList),2))

# Сокращенный вариант
list = [2, 3, 5, 9, 3]
print(sum(list[i] for i in range(len(list)) if i % 2 != 0))

