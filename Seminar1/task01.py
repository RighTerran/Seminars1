# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
number = int(input('Введите число соотвествующее дню недели: '))
if number >= 1 and number <= 5:
    print('Этот день не является выходным днем')
elif number >= 6 and number <= 7:
    print('Этот день является выходным днем')
else:
    print('Это число не соотвествует ни одному дню неделю, введите число от 1 до 7')