# игра крестики-нолики
import random

field = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

# варианты побед
vars_of_wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def print_field():
    print(field[0], field[1], field[2], end='\n')
    print(field[3], field[4], field[5], end='\n')
    print(field[6], field[7], field[8])


# передача символа в клетку
def step_field(step, symbol):
    ind = field.index(step)
    field[ind] = symbol

# Проверка на победителя
def get_result():
    win = ""

    for i in vars_of_wins:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win = "X"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            win = "O"

    return win

game_over = False
player = True # переменная для поочередного хода

while game_over == False:

    print_field()

    if player == True:
        symbol = "X"
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol = "O"
        while field[step-1] == "X" or field[step-1] == "O": # проверка на ход бота, пока клетка не будет свободной, подбор
            step = random.randint(1, 9)
        print(f'Бот: {step}')

    step_field(step, symbol)  # передача символа в ход с помощью символа
    win = get_result()  # проверка на победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player = not (player) # меняем порядок хода

print_field() # отобразить поле
print("Победил", win)
