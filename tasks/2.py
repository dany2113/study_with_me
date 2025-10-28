
# region 📚 Шпаргалка ЕГЭ | Задание №2

# Задание №1: https://inf-ege.sdamgia.ru/problem?id=56502
# Логическая функция F задаётся выражением:
# ((x→ y) ∨ (z → w)) ∧ ((z ≡ y) → (w ≡ x)).
#
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных w, x, y, z.

# Решение:
'''
print("x y z w")
for x in 0, 1:
    for y in range(2):
        for z in 0, 1:
            for w in range(2):
                F = (((x <= y) or (z <= w)) and ((z == y) <= (w == x)))
                if F == 0:
                    print(x, y, z, w)
'''

# Чистое решение кодом:
'''
from itertools import *

def F(x, y, z, w):
    return ((x <= y) or (z <= w)) and ((z == y) <= (w == x))


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(a1, 1, 0, a2), (0, 1, 0, 1), (a3, 1, 0, a4)]
    if len(set(table)) == len(table):
        for i in permutations('xyzw'):
            if [F(**dict(zip(i, r))) for r in table] == [0, 0, 0]:
                print(*i, sep='')

'''


# Задание №2: https://stepik.org/lesson/1038536/step/5?unit=1062771
# Логическая функция F задаётся выражением: (z ≡ ¬x) → ((w → ¬y) ∧ (y → x)).
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.

# Решение:
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in range(2):
            for w in range(2):
                F = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                if F == 0:
                    print(x, y, z, w, int(F))
                    
for x in range(2):
    for y in range(2):
        for z in 0, 1:
            for w in 0, 1:
                F = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                if F == 1:
                    print(x, y, z, w, int(F))
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 2 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1461
# endregion (не удаляйте меня, я тут не просто так)


# todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
# progress_result = ()  # Сюда заносятся номера, прорешанных задач.
# print('Рекомендуемое кол-во решенных задач для закрепления номера 30.')
# print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 30))}% задач прорешано.')

# n = int(input())
# print("Чётное" if n % 2 == 0 else "Нечётное")

# n = "41392"
# if (int(n[0])*int(n[2])) == int(n[1]) + int(n[3]) + int(n[4]):
#     print("Да")
# else:
#     print("Нет")

# n = int(input())
# if n > 80:
#     print("Почва пересыщена")
# elif 60<n<80:
#     print("Уровень влажности оптимален")
# elif 30<n<60:
#     print("Уровень влажности умеренный")
# else:
#     print("Почва слишком сухая")

# n = int(input())
# n1 = int(input())
# n2 = int(input())
# if n == n1 == n2:
#     print("Равносторонний")
# elif n == n1 or n1 == n2 or n2 == n:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# n = int(input())
# n1 = int(input())
# if n1 > n:
#     print("Делится" if n1 % n == 0 else "Не делится")
# elif n > n1:
#     print("Делится" if n % n1 == 0 else "Не делится")
# else:
#     print("Числа равны")

# l = []
# l1 = []
# for yer in range(0, 10000):
#     if yer % 4 == 0 or (yer % 100 != 0 and yer % 400 == 0):
#         l.append(yer)
#     else:
#         l1.append(yer)
# print(l)

# yer = int(input())
# if yer % 400 == 0 :
#     print("Високосный")
# elif yer % 4 == 0 and yer % 100 != 0:
#     print("Високосный")
# else:
#     print("Обычный")

# p = input()
# n = input()
# if n == p:
#     print("Пароль принят")
# n, y = "Информатика", "Физика"
# n1 = input()
# if n1 == n:
#     print("Петя берёт с собой компьютер")
# elif n1 == y:
#     print("Петя берёт с собой тетрадь")
# else:
#     print("Петя не возьмёт на физику компьютер")

# a = input()
# if len(a) >= 10 or len(a) % 2 == 0:
#     print("ДА")
# else:
#     print("НЕТ")

# n = int(input())
# n1 = int(input())
# n2 = int(input())
# if (n + n1 > n2) and (n1 + n2 > n) and (n + n2 > n1):
#     print("Да")
# else:
#     print("Нет")

# n = int(input())
# n1 = int(input())
# n2 = int(input())
# b = 0
# if (n % 7 == 0 or n % 40 == 0) and n % 49 != 0:
#     b += n
# if (n1 % 7 == 0 or n1 % 40 == 0) and n1 % 49 != 0:
#     b += n1
# if (n2 % 7 == 0 or n2 % 40 == 0) and n2 % 49 != 0:
#     b += n2
# print(b)



# print("x, y, z, w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#
#                 if ((w <= (not(z <= x))) or y) == False:
#                     print(x, y, z, w)
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (not(x <= z)) or (y == w) or y
                if F == 0:
                    print(x, y, z, w)
'''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (x and (not y)) or (x == z) or w
                if F == 0:
                    print(x, y, z, w)
'''
'''
print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = y and (x or z) or (not(y or z)) or w
                if F == 0:
                    print(x, y, z, w)
                  '''
'''
(x or y) and (not(y == z)) and (not w)
((x <= y) or (y == w)) and ((x or z) == w)
((y <= x) and (z or w)) <= ((x and (not w)) or (y == z))
'''
'''
print("x y z w")
for x in 0, 1:
    for z in 0, 1:
        for y in 0, 1:
            for w in 0, 1:
                F = (not( x <= w)) or (y <= z) or (not y)
                if F == 0:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x and (not y)) or (y == z) or (not w)
                if F == 0:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                if F == 0:
                    print(x, y, z, w)

print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                if F == 1:
                    print(x, y, z, w)'''
'''
print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (y <= (not(x <= z))) or w
                if F == 0:
                    print(x, y, z, w)
'''
'''
print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 1:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 0:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x <= y) or (z == x)) and (w <= z)
                if F == 1:
                    print(x, y, z, w)

print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x <= y) or (z == x)) and (w <= z)
                if F == 0:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (not(x or y)) and (not w) or (not(z or w)) and y
                if F == 1:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (not(x <= z)) or (y == w) or y
                if F == 0:
                    print(x, y, z, w)
 '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = ((x and y) == (not z)) and (y <= w)
                if F == 1:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x <= y) and (z or w)) <= ((x == w) or (y and (not z)))
                if F == 0:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (w <= (y == z)) and (y == (z <= x))
                if F == 1:
                    print(x, y, z, w)

print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (w <= (y == z)) and (y == (z <= x))
                if F == 0:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = ((x <= y) or (z == x)) and (w <= z)
                if F == 1:
                    print(x, y, z, w)

print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = ((x <= y) or (z == x)) and (w <= z)
                if F == 0:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 0:
                    print(x, y, z, w)

print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 1:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (x or (not y)) and z and (not w)
                if F == 1:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = ((x <= w) and ((not y) <= z)) <= ((z == x) or (w and (not y)))
                if F == 0:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (x and (not y)) or (y == z) or (not w)
                if F == 0:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (not(y <= x)) or (z <= w) or (not z)
                if F == 0:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = ((y and (x == (not z))) <= w) and (z <= y)
                if F == 0:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (x or (not y)) and (not(y == z)) and (not w)
                if F == 1:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (x <= y) and (z or (not w))
                if F == 1:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = ((z <= x) == (w <= y) or (x and w))
                if F == 0:
                    print(x, y, z, w)
                    '''
'''
print("x y z w")
for x in 0,1:
    for z in 0,1:
        for y in 0,1:
            for w in 0,1:
                F = (x <= y) and z and (not w)
                if F == 1:
                    print(x, y, z, w)
                    '''

# print("x y z w")
# for a in 0,1:
#     for b in 0,1:
#         for c in 0,1:
#             for d in 0,1:
#                 F = ((a or b) <= ((not c) and a)) and d
#                 if F == 1:
#                     print(a, b, c, d)

# print("t s r a")
# for t in 0, 1:
#     for s in 0, 1:
#         for r in 0, 1:
#             for a in 0, 1:
#                 F = (s or (not r)) and (not(r == a)) and t
#                 if F == 1:
#                     print(t, s, r, a)

# print("w x y z")
# for w in 0, 1:
#     for x in 0, 1:
#         for y in 0, 1:
#             for z in 0, 1:
#                 F = (not(x <= y)) or (z == w) or z
#                 if F == 0:
#                     print(w, x, y, z)
#
# print("w x y z")
# for w in 0, 1:
#     for x in 0, 1:
#         for y in 0, 1:
#             for z in 0, 1:
#                 F = (not(((not x) or w) and (not y))) or (not(z and (not(w and y))))
#                 if F == 0:
#                     print(w, x, y, z)

# print("x y z w")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 F = z or (x == (y <= w))
#                 if F == 0:
#                     print(x, y, z, w)
#
# print("w x y z")
# for w in 0,1:
#     for x in 0,1:
#         for y in 0,1:
#             for z in 0,1:
#                 for F in 0,1:
#                     if (((not w) <= x) <= (y and z) and (x == (not w))):
#                         if F == 1:
#                             print(w, x, y, z)

# print("x y z w")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 F = (not z) and (not(y and (not x))) and (not(x == w))
#                 if F == 1:
#                     print(x, y, z, w)

# print("x y z w")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 F = (not(((not x) or y) and (not w))) or (not ( z and (not( y and w))))
#                 if F == 0:
#                     print(x, y, z, w)

# print("x y z w")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 F = (w <= (not(z <= x))) or y
#                 if F == 0:
#                     print(x, y, z, w)
#
# print("x y z w")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 F = (not(w <= (x == y))) and (z <= x)
#                 if F == 1:
#                     print(x, y, z, w)

# print("x y z w")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 F = (not(y <= x)) or (z <= w) or (not z)
#                 if F == 0:
#                     print(x, y, z , w)

# print("x y z w")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 F = (not(y <= (x == z))) and (w <= x)
#                 if F == 1:
#                     print(x, y, z, w)

# print("x y z w")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 F = x and (w == (z == y and w))
#                 if F == 1:
#                     print(x, y, z, w)