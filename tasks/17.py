
# region 📚 Шпаргалка ЕГЭ | Задание №17

# Задание №1:
# В файле содержится последовательность натуральных чисел.
# Элементы последовательности могут принимать целые значения от 1 до 100 000 включительно.
# Определите количество пар последовательности, в которых хотя бы одно число делится на
# минимальный элемент последовательности, кратный 21.
# Гарантируется, что такой элемент в последовательности есть.
# В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

# Решение:
'''
M = [int(i) for i in open('17.txt')]
D = [int(i) for i in M if i % 21 == 0]
R = []
for i in range(len(M) - 1):
    x, y = M[i:i+2]
    if (x % min(D) == 0) or (y % min(D) == 0):
        R.append(x + y)
print(len(R), max(R))
'''


# Задание №2:
# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от —100 000 до 100 000 включительно.
# Определите количество троек элементов последовательности, в которых хотя бы один из трёх элементов оканчивается на 3,
# а сумма элементов тройки не больше максимального элемента последовательности, являющегося пятизначным числом,
# которое оканчивается на 3.
# В ответе запишите количество найденных троек чисел,
# затем максимальную из сумм элементов таких троек.
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.

# Решение:
'''
M = [int(i) for i in open('17.txt')]
D = [i for i in M if str(i)[-1] == '3']
B = [i for i in D if len(str(i)) == 5]
R = []
for i in range(len(M) - 2):
    x, y, z = M[i:i+3]
    if (x in D) or (y in D) or (z in D):
        R.append(x + y + z)
print(len(R), max(R))
'''


# Задание №3:
# В файле содержится последовательность целых неотрицательных чисел, не превышающих 10000.
# Определите количество пар элементов последовательности, в которых либо сумма элементов кратна 18,
# либо произведение элементов кратно 18.
# В ответе запишите два числа: сначала количество найденных пар, затем максимальную сумму элементов этих пар.
# В данной задаче под парой подразумевается два различных элемента последовательности.

# Решение:
'''
M = [int(i) for i in open('17.txt')]
R = []
for i in range(len(M)):
    for j in range(i + 1, len(M)):
        x, y = M[i], M[j]
        if ((x + y) % 18 == 0) or ((x * y) % 18 != 0):
            R.append(x + y)
print(len(R), max(R))
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 17 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1612
# 💡 Генераторы списков (списочные выражения) для ЕГЭ: https://t.me/informatika_kege_itpy/339
# 💡 Работа с файлами Python: https://t.me/informatika_kege_itpy/286
# 🐍 Примеры работы с .txt файлами на некоторых номерах ЕГЭ: https://t.me/informatika_kege_itpy/400
# 🐍 Шпаргалка по генераторам списков: https://t.me/informatika_kege_itpy/495
# endregion (не удаляйте меня, я тут не просто так)


# # todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
# progress_result = ()  # Сюда заносятся номера, прорешанных задач.
# print('Рекомендуемое кол-во решенных задач для закрепления номера 50.')
# print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 50))}% задач прорешано.')

# общая заметка
# a = []
# for i in range(1000, 5000):
#     if i % 3 == 0 and str(i)[3] == "5" and str(i)[1] == "3":
#         a.append(i)
# print(min(a), max(a))

# a = []
# for i in range(10000, 60000):
#     if i % 4 == 0:
#         if str(i)[1] == "2" and str(i)[-2] == "5":
#             a.append(i)
# print(min(a), max(a))


# A = [4, 7, 1, 1, 6, 2, 5, 9, 1]
# B = [A[i] for i in range(1, len(A)) if A[i] <= A[0]]
# print(len(B))

# n = 6
# a = [i // 2 if i % 2 == 0 else (i + 1) // 2 for i in range(2, n+1)]
# print(sum(a)) тернарное написание генератора (if else впереди)

# from random import *
#
# a = [randint(1, 50) for i in range(20)]
# ans = []
# for x in a:
#     ans = [x if x % 6 == 3 else 0]
# print(sum(ans))

# функция map()
# map(действие, объект итерирования) применяет основное требование на весь список
# map  не возвращает список, поэтому добавляем перед функцией list как пример


# a = [int(i) for i in open("files/17_18932.txt")]
# v = [x for x in a if x % 2 == 0]
# l = [x for x in a if x > 0]
# r = []
# for i in range(len(a)-1):
#     x, y = a[i], a[i+1]
#     if (x in l) + (y in l) >= 1:
#         if (x + y) < len(v):
#             r.append(x**2 + y**2)
# print(len(r), max(r))


# a = [int(i) for i in open("files/17_24065.txt")]
# m = min([x for x in a if len(str(x)) == 3])
# b = [x for x in a if len(str(x)) == 3]
# l = []
# for i in range(len(a) - 1):
#     x, y = a[i], a[i+1]
#     if (x in b) + (y in b) == 1:
#         if (x + y) % m == 0:
#             l.append(x + y)
# print(len(l), max(l))

# a = [int(i) for i in open("files/17_22230.txt")]
# p = []
# l = [x for x in a if len(str(abs(x))) == 4]
# m = max([x for x in a if abs(x) % 25 == 0])
# k = [x for x in a if x > 0]
# k1 = min([x for x in k if str(x)[-1] == "8"])
# for i in range(len(a)-2):
#     x, y, z = a[i], a[i+1], a[i+2]
#     if (x in l) + (y in l) + (z in l) == 2:
#         if (x % k1 == 0) + (y % k1 == 0) + (z % k1 == 0) >= 1:
#             if (x + y + z) >= m:
#                 p.append(x + y + z)
# print(len(p), max(p))

# a = [int(i) for i in open("files/17_19249.txt")]
# patizn = [x for x in a if (len(str(abs(x)))) == 5 and str(x)[-2:] == "43"]
# patizn1 = max([x for x in a if (len(str(abs(x)))) == 5 and str(x)[-2:] == "43"])**2
# l = []
# for i in range(len(a) - 2):
#     x, y, z = a[i], a[i+1], a[i+2]
#     if (x in patizn) + (y in patizn) + (z in patizn) >= 1:
#         if x**2 + y**2 + z**2 <= patizn1:
#             l.append(x**2+y**2+z**2)
# print(len(l), min(l))

# a = [int(i) for i in open("files/17_17558 (1).txt")]
# print(a)
# p = []
# l = [x for x in a if x < 0]
# m = len([x for x in a if x % 32 == 0])
# for i in range(len(a) - 1):
#     x, y = a[i], a[i+1]
#     if (x in l) + (y in l) == 1:
#         if x + y < m:
#             p.append(x + y)
# print(len(p), max(p))
#
# a = [int(i) for i in open("files/17____23447.txt")]
# l = []
# l1 = [x for x in a if len(str(abs(x))) == 4]
# l2 = max([x for x in l1 if str(x)[-2:] == "39"])
# for i in range(len(a) - 1):
#     x, y = a[i], a[i+1]
#     if (x in l1) + (y in l1) == 1:
#         if (x + y)**2 < l2**2:
#             l.append(x+y)
# print(len(l), max(l))


# a = [int(i) for i in open("files/17_24235.txt")]
# m = [x for x in a if abs(len(str(x))) == 4]
# m1 = max([x for x in a if abs(len(str(x))) == 4])
#
# l = []
# for i in range(len(a)- 1): ******
#     x, y = a[i], a[i+1]
#     if (x in m) + (y in m) == 1:
#         if (x * y) % m1 == 0:
#             l.append(abs(x*y))
# print(len(l), l) ******* №24235 опечатка; минимальное \ максимальное

# a = [int(i) for i in open("files/17_23376 (2).txt")]
# m1 = [x for x in a if len(str(abs(x))) == 5]
# m2 = max([x for x in m1 if x%100 == 37])
# l = []
# for i in range(len(a)-1):
#     x, y = a[i], a[i+1]
#     if (x in m1) + (y in m1) == 1:
#         if (x + y)**2 > m2**2:
#             l.append(x+y)
# print(len(l), max(l))
#
# a = [int(i) for i in open("files/17 (2).txt")]
# m1 = len([x for x in a if x < 0 and x % 3 == 0])
# l = []
# for i in range(len(a)-1):
#     x, y = a[i], a[i+1]
#     if (x > 0) + (y < 0) == 2 or (x < 0) + (y > 0) == 2:
#         if abs(x - y) % m1 == 0:
#             l.append(x+y)
# print(len(l), max(l))
