import random

player = int(input("1 - Камень, 2 - Ножницы, 3 - Бумага. "))
if player == 1:
    print("Игрок - Камень")
elif player == 2:
    print("Игрок - Ножницы")
elif player == 3:
    print("Игрок - Бумага")
else:
    print("Ошибка")

bot = random.randint(1, 3)
if bot == 1:
    print("Бот - Камень")
elif bot == 2:
    print("Бот - Ножницы")
elif bot == 3:
    print("Бот - Бумага")

if player == bot:
    print("Ничья")
elif player == 1 and bot == 2:
    print("Вы победили!")
elif player == 1 and bot == 3:
    print("Победил бот!")
elif player == 2 and bot == 1:
    print("Победил бот!")
elif player == 2 and bot == 3:
    print("Вы победили!")
elif player == 3 and bot == 1:
    print("Вы победили!")
elif player == 3 and bot == 2:
    print("Победил бот!")