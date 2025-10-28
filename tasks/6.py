
# region 📚 Шпаргалка ЕГЭ | Задание №6

# Задание №1:
# Исполнитель Черепаха действует на плоскости с декартовой системой координат.
# В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления
# оси ординат, хвост опущен.
#
# Черепахе был дан для исполнения следующий алгоритм:
# Направо 120 Повтори 8 [Вперёд 4 Направо 60].
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией,
# заданной данным алгоритмом. Точки на линии учитывать не следует.

# Решение:
'''
import turtle as t
t.left(90)
t.tracer(0)
l = 30

t.right(120)
for _ in range(8):
    t.forward(4 * l)
    t.right(60)

t.up()
for x in range(-20, 20):
    for y in range(-20, 1):
        t.goto(x * l, y * l)
        t.dot('black')
t.done()
'''
import turtle

# Задание №2:
# Исполнитель Черепаха действует на плоскости с декартовой системой координат.
# В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси
# ординат, хвост опущен.
#
# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 2 [Вперёд 7 Направо 60 Вперёд 12 Направо 120]
# Поднять хвост
# Вперёд 7 Направо 60
# Опустить хвост
# Повтори 2 [Вперёд 5 Направо 120 Вперёд 10 Направо 60]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри пересечения фигур,
# ограниченных заданными алгоритмом линиями, не включая точки на границах этого пересечения.

# Решение:
'''
import turtle as t
t.left(90)
t.tracer(0)
l = 30

t.color('teal')
for _ in range(2):
    t.forward(7 * l)
    t.right(60)
    t.forward(12 * l)
    t.right(120)

t.up()
t.forward(7 * l)
t.right(60)
t.down()

t.color('purple')
for _ in range(2):
    t.forward(5 * l)
    t.right(120)
    t.forward(10 * l)
    t.right(60)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * l, y * l)
        t.dot('black')
t.done()
'''


# Задание №3:
# Исполнитель Черепаха действует на плоскости с декартовой системой координат.
# В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси
# ординат, хвост опущен.
#
# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 2 [Вперёд 9 Направо 90 Вперёд 15 Направо 90]
# Поднять хвост
# Вперёд 12 Направо 90
# Опустить хвост
# Повтори 2 [Вперёд 6 Направо 90 Вперёд 12 Направо 90]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри объединения фигур,
# ограниченных заданными алгоритмом линиями, не включая точки на границах этого объединения.

# Решение:
'''
import turtle as t
t.left(90)
t.tracer(0)
l = 30

t.color('teal')
for _ in range(2):
    t.forward(9 * l)
    t.right(90)
    t.forward(15 * l)
    t.right(90)
t.up()
t.forward(12 * l)
t.right(90)
t.down()
t.color('purple')
for _ in range(2):
    t.forward(6 * l)
    t.right(90)
    t.forward(12 * l)
    t.right(90)

t.up()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x * l, y * l)
        t.dot('black')
t.done()
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 6 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1466
# 💡 Библиотека Turtle, чем может быть полезна на ЕГЭ: https://t.me/informatika_kege_itpy/407
# 🐍 Рисование и управление экраном в Turtle: https://t.me/informatika_kege_itpy/410
# 🐍 Пять простейших функций из библиотеки Turtle в Python: https://t.me/informatika_kege_itpy/408
# 🐍 Функции для управления положением черепахи на экране:  https://t.me/informatika_kege_itpy/409
# endregion (не удаляйте меня, я тут не просто так)


# todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
# progress_result = ()  # Сюда заносятся номера, прорешанных задач.
# print('Рекомендуемое кол-во решенных задач для закрепления номера 20.')
# print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 20))}% задач прорешано.')


# from turtle import *
# tracer(0)
# screensize(5000, 5000)
# r = 15
#
# for i in range(5):
#     forward(37*r); rt(90); forward(44*r); rt(90)
# up()
# back(18*r); rt(90); forward(29*r); lt(90)
# down()
# for i in range(5):
#     forward(31*r); rt(90); forward(35*r); rt(90)
# up()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*r, y*r)
#         dot(3, "red")
# turtle.mainloop()
# done()

# import turtle as t
#
# t.tracer(0)
# t.screensize(5000, 5000)
# r = 50
#
# t.rt(30)
# for i in range(3):
#     t.rt(150); t.fd(6*r); t.rt(30); t.fd(12*r)
# t.up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         t.goto(x*r, y*r)
#         t.dot(3, "red")
# t.mainloop()
# t.done()

# import turtle as t
#
# t.tracer(0)
# t.screensize(5000, 5000)
# r = 15
#
# for i in range(9):
#     t.fd(27*r); t.rt(90); t.fd(30*r); t.rt(90)
# t.up()
# t.fd(3*r); t.rt(90); t.fd(6*r); t.lt(90)
# t.down()
# for i in range(9):
#     t.fd(77*r); t.rt(90); t.fd(66*r); t.rt(90)
# t.up()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         t.goto(x*r,y*r)
#         t.dot(3, "red")
# t.mainloop()
# t.done()



# from turtle import *
#
# tracer(0)
# screensize(5000, 5000)
# r = 25
# for i in range(3):
#     fd(27*r); rt(90); fd(12*r); rt(90)
# up(); fd(4*r); rt(90); fd(6*r); lt(90)
# down()
# for i in range(4):
#     fd(83*r); rt(90); fd(77*r); rt(90)
# up()
#
# for x in range(-60, 100):
#     for y in range(-100, 100):
#         goto(x*r, y*r)
#         dot(3, "red")
# turtle.mainloop()
# down()
# print(28*13) 364
# print(84*78) 6552
# print((364+6552) - (7*24))
# print(1280*960*11) 13516800
# print(96468992/13516800)

# from turtle import *
#
# tracer(0)
# screensize(5000, 5000)
# r = 25
#
# for i in range(5):
#     fd(15*r); lt(90); fd(25*r); lt(90)
# up(); fd(4*r); lt(90); fd(12*r); lt(90)
# down()
# for i in range(6):
#     fd(38*r); rt(90); fd(22*r);rt(90)
# up()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*r, y*r)
#         dot(3, "red")
#
# turtle.mainloop()


# from turtle import *
# tracer(0)
# screensize(5000, 5000)
# r = 25
#
# for i in range(13):
#     fd(13*r); rt(90); fd(5*r)
# up()
# rt(90); fd(7*r); lt(90); fd(10*r)
# down()
# for i in range(23):
#     fd(8*r); lt(90); fd(11*r); lt(90)
# up()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * r, y * r)
#         dot(3, "red")
# turtle.mainloop()

# from turtle import *
# tracer(0)
# screensize(5000, 5000)
# r = 25
#
# for i in range(2):
#     fd(28*r); rt(90); fd(18*r); rt(90)
# up(); fd(14*r); rt(90);fd(10*r);lt(90)
# down()
# for i in range(2):
#     fd(30*r); rt(90); fd(7*r); rt(90)
# up()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * r, y * r)
#         dot(3, "red")
# turtle.mainloop()

# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# r = 25
#
# for i in range(3):
#     fd(10*r); rt(90); fd(15*r); rt(90)
# up(); fd(4*r); rt(90); fd(7*r); lt(90)
# down()
# for i in range(2):
#     fd(80*r); rt(90); fd(60*r); rt(90)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * r, y * r)
#         dot(3, "red")
#
# turtle.mainloop()

# from turtle import *
# tracer(0)
# screensize(5000, 5000)
# r = 25
#
# for i in range(3):
#     fd(25*r); lt(90); fd(30*r); lt(90)
# up()
# fd(20*r); rt(90); back(7*r); lt(90)
# down()
# for i in range(3):
#     fd(60*r); rt(90); fd(30*r); rt(90)
# up()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*r, y*r)
#         dot(3, "red")

# turtle.mainloop()

#
# from turtle import *
# tracer(0)
# screensize(5000, 5000)
# r = 25
#
# for i in range(6):
#     fd(7*r); rt(45); fd(4*r); rt(90); fd(4*r); rt(45)
# up()
# fd(1*r); rt(90); back(20*r)
# down()
# for i in range(5):
#     fd(24*r); lt(90); fd(6*r); lt(90)
# up()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * r, y * r)
#         dot(3, "red")
#
# turtle.mainloop()

#
# from turtle import *
# tracer(0)
# screensize(5000, 5000)
# r = 25
#
# for i in range(8):
#     fd(16*r); rt(90); fd(22*r); rt(90)
# up()
# fd(5*r); rt(90); fd(5*r); lt(90)
# down()
# for i in range(8):
#     fd(52*r); rt(90); fd(77*r); rt(90)
# up()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * r, y * r)
#         dot(3, "red")
#
# turtle.mainloop()

#
# from turtle import *
# tracer(0)
# screensize(5000, 5000)
# r = 15
#
# for i in range(4):
#     fd(10*r); rt(270)
# up(); fd(3*r); rt(270);fd(5*r); rt(90)
# down()
# for i in range(2):
#     fd(10*r); rt(270); fd(12*r); rt(270)
# up()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * r, y * r)
#         dot(3, "red")
# turtle.mainloop()

# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# r = 25
#
# for i in range(3):
#     fd(27*r); rt(90); fd(12*r); rt(90)
# up(); fd(4*r); rt(90); fd(6*r); lt(90)
# down()
# for i in range(4):
#     fd(83*r); rt(90); fd(77*r); rt(90)
# up()
#
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x * r, y * r)
#         dot(3, "red")
#
# turtle.mainloop()
#
# print((28 * 12 + 84 * 77) - 24 * 6)

# from turtle import *
# tracer(0)
# screensize(5000, 5000)
# r = 25
#
# for i in range(5):
#     fd(40*r); rt(90); fd(46*r); rt(90)
# up(); fd(19*r); rt(90); fd(19*r); lt(90)
# down()
# for i in range(5):
#     fd(37*r); rt(90); fd(19*r); rt(90)
# up()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*r, y*r)
#         dot(3, "red")
# turtle.mainloop()
#
# from turtle import *
# tracer(0)
# screensize(5000, 5000)
# r = 25
#
# for i in range(3):
#     fd(39*r); rt(90); fd(48*r); rt(90)
# up(); fd(27*r); rt(90); fd(24*r); lt(90)
# down()
# for i in range(3):
#     fd(29*r); rt(90); bk(18*r); rt(90)
# up()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*r, y*r)
#         dot(3, "red")
#
# turtle.mainloop()


from turtle import *
tracer(0)
screensize(5000, 5000)
r = 25

for i in range(24):
    fd(10*r); rt(90); fd(5*r)
up(); lt(90); fd(7*r); rt(90)
down()
for i in range(22):
    fd(8*r); rt(90); fd(20*r); rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*r, y*r)
        dot(3, "red")

turtle.mainloop()