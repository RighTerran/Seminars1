def calculator(a, b):
    point = input('\tВведите знак: ')
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