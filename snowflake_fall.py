import random
import time
import os

# Определение символов для снежинки и пустого пространства
snowflake = "❄️"
empty_space = ""

#   Определение высоты и ширины поля
height = 20
width = 50

# Создание пустого поля с помощью генератора

field = [[empty_space for _ in range(width)] for _ in range(height)]

# Очистка терминала

os.system("cls" if os.name == "nt" else "clear")

# Функция для отображения поля

def display_field(field):
    for row in field:
        print("".join(row))


# Переодическое обновление состояния поля и егоотображение

while True:
    os.system("slc" if os.name == "nt" else "clear") 

# Определение случайных координат для снежинки
    x = random.randint(0, width - 1)
    y = random.randint(0, height -1)

    # падение снежинки до дна поля

    while y < height - 1 and field[y + 1][x] == empty_space:
        field[y][x] = empty_space
        y += 1
        field[y][x] = snowflake

    # отображение обновления поля 

    display_field(field)    

    # Задержкамежду кадрами

    time.sleep(0.1)












