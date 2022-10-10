import random

class color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

k = 2021 # конфеты
m = 28
print(f'Первому игроку нужно взять {k % (m + 1)} конфет') # ответ на вопрос в задаче

#Разработка игры
igrok1 = input('Введите имя игрок №1: ')
igrok2 = 'Bot'

# жребий для игрока и бота
while True:
    print(f'{igrok1}, введите число от 1 до 100: ')
    igrok1_digit = int(input())
    igrok2_digit = int(random.randint(1, 101))
    print(f'{igrok2}, число: {igrok2_digit}')
    if igrok1_digit > igrok2_digit:
        print(f'Первым ходит {igrok1}')
        break
    elif igrok1_digit < igrok2_digit:
        print(f'Первым ходит {igrok2}')
        break
    else:
        igrok1_digit == igrok2_digit == False # вариант при котором у обоих одинаковые значения

count = 1
print('Введите число от 1 до 28: ')
while k != 0:
    print(f'\n{color.BOLD}Ход №{count}: {color.END}')
    player1 = -1 # значение для входа в цикл
    while player1 <= 0 or player1 >= 29: # проверка на ограничение во взятии конфет от 1 до 28
        player1 = int(input('Игрок №1: '))
    k = k - player1 # уменьшаем общее количество конфет
    print(f'{color.RED}Конфет осталось {k}{color.END}')
    if k == 0:
        print(color.GREEN + 'Игрок №1 Победил!' + color.END)
        break
    if k <= 28: # наделяем интелектом бота, когда меньше 28, чтобы забирал все что есть
        player2 = k
        print(f'Игрок №2: {player2}')
        k = k - player2
        print(f'{color.RED}Конфет осталось {k}{color.END}')
        print(color.GREEN + 'Игрок №2 Победил!' + color.END)
        break
    player2 = int(random.randint(1, 28)) # ход бота
    print(f'Игрок №2: {player2}')
    k = k - player2 # уменьшаем общее количество конфет
    print(f'{color.RED}Конфет осталось {k}{color.END}')
    if k == 0:
        print(color.GREEN + 'Игрок №2 Победил!' + color.END)
    count += 1 # цикл для количество Ходов