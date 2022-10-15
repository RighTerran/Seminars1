def Complex_cal(a, b):
    a1 = int(input('\tВведите действительную часть первого числа: '))
    b1 = int(input('\tВведите мнимую часть первого числа: '))
    c1 = complex(a1, b1)  # формируем комплексное число

    a2 = int(input('\tВведите действительную часть второго числа: '))
    b2 = int(input('\tВведите мнимую часть второго числа: '))
    c2 = complex(a2, b2)  # формируем комплексное число

    print(f'Комлексное число №1: {c1}')
    print(f'Комлексное число №2: {c2}\n')
    point = input('Введите знак: ')
    if point == '+':
        print('Addition =', a + b)
    elif point == '-':
        print('Subtraction =', a - b)
    elif point == '*':
        print('Multiplication =', a * b)
    elif point == '/':
        if b == 0:
            print("Деление на 0 не допускается")
        else:
            print('Division =', a / b)
