
# region 📚 Шпаргалка ЕГЭ | Задание №11

# Задание №1:
# При регистрации в компьютерной системе каждому объекту присваивается идентификатор, состоящий из 235 символов и
# содержащий символы из 30-символьного набора букв.
# В базе данных для хранения каждого идентификатора отведено одинаковое и минимально возможное целое число бит.
# При этом используется посимвольное кодирование идентификаторов,
# все символы кодируются одинаковым и минимально возможным количеством бит.
# Определите объём памяти (в Мбайт), необходимый для хранения 71 698 идентификаторов.
# В ответе запишите только целую часть числа.

# Решение:
'''
symbols = 235
alphabet = 30
i = 5
bit = symbols * i
mbyte = (bit * 71698) / 2 ** 23
print(mbyte)
'''


# Задание №2:
# При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из 35 символов
# и содержащий только десятичные цифры и символы из 4090-символьного специального алфавита.
# В базе данных для хранения сведений о каждом пользователе отведено одинаковое и минимально возможное целое число байт.
# При этом используют посимвольное кодирование паролей, все символы кодируют одинаковым и минимально возможным
# количеством бит.
# Кроме собственно пароля, для каждого пользователя в системе хранятся дополнительные сведения,
# для чего выделено целое число байт; это число одно и то же для всех пользователей.
# Для хранения сведений о 300 пользователях потребовалось 96000 байт.
# Сколько байт выделено для хранения дополнительных сведений об одном пользователе?
# В ответе запишите только целое число – количество байт.

# Решение:
'''
symbols = 35
alphabet = 4090 + 10
i = 13
bit = symbols * i
byte = int(bit / 8) + 1
all_info = 96000 / 300
dop_info = all_info - byte
print(dop_info)
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 11 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1496
# 💡 Учимся работать с единицами измерения информации: https://t.me/informatika_kege_itpy/386
# endregion (не удаляйте меня, я тут не просто так)

#
# # todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
# progress_result = ()  # Сюда заносятся номера, прорешанных задач.
# print('Рекомендуемое кол-во решенных задач для закрепления номера 30.')
# print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 30))}% задач прорешано.')

# from math import *
# for A in range(1, 1000):
#     both = log2(A)
#     vel = ceil((248*both)/8)
#     if vel * 75600 > 16 * 1024 * 1024:
#         print(A)
#         break

# from math import *
# k = log2(1048576)
# k1 = log2(32)
# alf = 1000
# print((alf*k)//(alf*k1))

# from math import *
# alf = 26*2 + 10
# both = log2(alf)
# simb = ceil((18 * both) / 8)
# print(simb*50)

# from math import *
# a = 10 + 10*2
# both = log2(a)
# sim = ceil((both * 25) / 8)
# print(sim*40)

# from math import *
# A = 1024
# both = log2(A)
# sim1 = ceil((both*300) / 8)
# sim2 = ceil((sim1*32768) / 1024)
# print(sim2)

# from math import *
# a = 512
# both = log2(a)
# sim1 = ceil((both*450) / 8)
# sim2 = ceil((16384 * sim1) / 1024)
# print(sim2)

# from math import *
# a = 26 + 10
# bdb = ceil(log2(a))
# print(bdb)
# nom = ceil((24 * bdb) / 8)
# print(nom)
# print(nom*100)

# from math import *
# a = ceil(log2(262144))
# a1 = log2(64)
# print(ceil(a/a1))

# from math import *
# alf = 256
# both = ceil(log2(2023+10))
# simb = ceil((both*alf) / 8)
# sim = ceil((32768 * simb) / 1024)
# print(sim)

# from math import *
# alf = 315
# both = ceil(log2(5000))
# simb = ceil((both*alf) / 8)
# sim = ceil((262144*simb) / 1024)
# print(sim)

# from math import *
# alf = 26
# both = ceil(log2(alf))
# simb = ceil((both*20) / 8)
# sim = simb*50
# print(sim)

# from math import *
# alf = 26*2 + 10 + 6
# both = ceil(log2(alf))
# kod = ceil((25 * both) / 8)
# nomer = ceil(log2(2000))
# k = ceil(nomer / 8)
# prop = 50 - (k + kod)
# print(k, kod, prop)


# from math import *
# alf = 26*2 + 10
# both = ceil((log2(alf)))
# sim1 = ceil((both * 10) / 8)
# nomer = ceil(log2(500))
# nom = ceil(nomer / 8)
# V = 40 + nom + sim1
# print(V)

# from math import *
# for x in range(2, 100000):
#     alf = ((2 * 68000 * 295 * ceil(log2(x))) * 22) + 1712128
#     if alf // 14680074 <= 500:
#         print(log2(x))

# from math import *
# for x in range(2, 10000):
#     alf = (1050 * 460 * ceil(log2(x))) * 64
#     if alf // 1474560 <= 200:
#         print(x)

# from math import *
# for x in range(2, 100000):
# alf = (128000 * 16 * 4 * x) // 8 // 1024 // 1024
# if alf == 64:
#     print(x)
#
# alf1 = (32000 * 4 * 2 * 66) // 8 // 1024 // 1024
# print(alf1)

# from math import *
# for x in range(2, 10000):
#     alf = (8000 * 16 * 4 * x) // 8 // 1024 // 1024
#     if alf == 7:
#         print(x)

# for x in range(2, 10000):
#     alf = (x * 2 * 15000 * 16 * 15) // 8 // 1024 // 1024
#     if alf <= 125:
#         print(x)

# a = 4096*8192*24*0.65 + 64*2**13
# b = 5 * 2**33 / a
# print(b)

# a = 3840 * 2160 * 24 * 0.65 + 120 * 2**13
# n = 4320
# b = 20 * 2**33
# m = b // a
# m1 = n / m
# print(m1)
#
# al = (2 * 48000 * 32 * 150) // 1280000
# al1 = (2 * 32000 * 16 * 150) // 1280000
# print(240/ 60)

# a = (1920 * 1080 * 23 * 120) // 8 // 1024
# a1 = (1280 * 1024 * 21 * 120) // 8 // 1024
# print(a - a1)

# from math import *
# al = 10 + 52 + 5478
# both = ceil(log2(al))
# odinnom = (693 * 1024) / 2000
# p = 2840 / both
# print(p)

# from math import *
# alf = 10 + 26 + 470
# for dlin in range(1, 10000):
#     both = ceil(log2(alf))
#     if dlin * both * 2500 > 61 * 1024 * 8:
#         print(dlin)
#         break

# from math import *
# alf = 10 + 52 + 454
# both = ceil(log2(alf))
# for x in range(1, 1000000):
#     if x * 31922 * both > 2 * 1024 * 1024 * 1024 * 8:
#         print(x)
#         break

# from math import *
# for x in range(1, 10000):
#     alf = 3425
#     borh = ceil(log2(x))
#     if (alf * borh) * 2718281 >= 9 * 2**33:
#         print(x)
#         break

# from math import *
# kod = 94
# for x in range(1, 10000000):
#     alf = (kod * x) / 8
#     if alf * 205000 >= 7 * 1024 * 1024:
#         print(x)
#         break

# from math import *
# both = ceil(log2(33))
# l = 5536*1024
# k = (377*6* 23155) / 8
# print(l, k)

# from math import *
# for dlin in range(1, 10000):
#     alf = 10 + 52 + 4044
#     both = ceil(log2(alf))
#     if (both*dlin*7777) <= 566 * 1024 * 8:
#         print(dlin)

# from math import *
# for alf in range(1, 1000000):
#     both = ceil(log2(alf))
#     if alf * both * 75600 > 16 * 2**33:
#         print(alf, both)
#         break

# for dlin in range(1, 10000):
#     if ((11 * dlin)) * 2000 < 693 * 2**13:
#         print(dlin)


# for alf in range(1, 10000):
#     if ((5*alf) // 8) * 7564230 > 31 * 1024 * 1024:
#         print(alf)
#         break
#
# l1 = 31 * 1024 * 1024
# l2 = ((5*8) / 8) * 7_564_230
# l21 = ((5*8) // 8) * 7_564_230
# l3 = ((5*7) / 8) * 7_564_230
# l31 = ((5*7) // 8) * 7_564_230
# print(l1, l2, l3, l21, l31)

from math import *
for alf in range(1, 10000):
    both = (ceil(alf)*270) / 8
    if both * 100_000 > 32*1024*1024:
        print(alf)
        break