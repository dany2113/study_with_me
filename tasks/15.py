# region 📚 Шпаргалка ЕГЭ | Задание №15

# Задание №1:
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наименьшего натурального числа А формула (ДЕЛ(x,2) → ¬ДЕЛ(x,13)) ∨ (x + A ≥ 1000)
# тождественно истинна (т.е. принимает значение 1) при любом натуральном значении переменной х?

# Решение:
'''
def F(x, A):
    return (x % 2 == 0) <= (x % 13 != 0) or ((x + A) >= 1000)

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 1000)):
        print(A)
        break
'''

# Задание №2:
# На числовой прямой даны два отрезка: P = [10, 35] и Q = [17, 48].
# Укажите наибольшую возможную длину отрезка A, для которого формула
# ((x принадлежит A) → ¬(x принадлежит P)) → ((x принадлежит A) → (x принадлежит Q))
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

# Решение:
'''
def F(x):
    P = 10 <= x <= 35
    Q = 17 <= x <= 48
    A = a1 <= x <= a2
    return (A <= (not P)) <= (A <= Q)

M = [i / 4 for i in range(1 * 4, 60 * 4)]
R = []
for a1 in M:
    for a2 in M:
        if all(F(x) for x in M):
            R.append(a2 - a1)
print(max(R))
'''

# Задание №3:
# Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Для какого наименьшего неотрицательного целого числа А формула x&25 != 0 → (x&17 = 0 → x&А != 0)
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной х)?

# Решение:
'''
def F(x):
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))

for A in range(0, 1000):
    if all(F(x) for x in range(0, 1000)):
        print(A)
        break
'''

# Задание №4:
# При каком наибольшем целом A найдутся такие целые неотрицательные x и y, что выражение (3x+y>48)∨(x>y)∨(4x+y<A)
# будет ложным?

# Решение:
'''
def F(x, y, A):
    return ((3 * x) + y > 48) or (x > y) or ((4 * x) + y < A)

R = []
for A in range(0, 100):
    if any(F(x, y, A) == 0 for x in range(0, 100) for y in range(0, 100)):
        R.append(A)
print(max(R))
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 15 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1550
# 💡 Условные операторы if, else, elif а также логические операторы and и or: https://t.me/informatika_kege_itpy/294
# 💡 Функции all() и any(), где они могут пригодиться на ЕГЭ: https://t.me/informatika_kege_itpy/378
# 💡 Множества set в Python: https://t.me/informatika_kege_itpy/242
# 💡 Циклы for и while, как использовать циклы для сдачи КЕГЭ: https://t.me/informatika_kege_itpy/169
# endregion (не удаляйте меня, я тут не просто так)

#
# # todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
# progress_result = ()  # Сюда заносятся номера, прорешанных задач.
# print('Рекомендуемое кол-во решенных задач для закрепления номера 40.')
# print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 40))}% задач прорешано.')


# def f(x, y, A):
#     return (x < A) and (y < 3*A) or(2*x + y > 128)
# R = []
# for A in range(0, 100):
#     if any(f(x, y,  A) == 0 for x in range(0,100) for y in range(0, 100)):
#         R.append(A)
# print(R)

# B = list(range(36, 76))
# C = list(range(60, 110))
# a = []
# for x in range(-100, 1000):
#     if not(x not in a) <= ((x in B) == (x in C)):
#         a.append(x)
# print(a)

# P = list(range(52, 106))
# Q = list(range(0, 54))
# a = []
# for x in range(0, 1000):
#     if not((x not in P) and (x not in Q) and (x not in a)) <= (x**2 > 303601):
#         a.append(x)
# print(a[-1]-a[0])

# P = list(range(10, 151))
# Q = list(range(160, 251))
# R = list(range(240, 301))
# a = []
# for x in range(-100, 1000):
#     if not(((x in Q) <= (x in P)) or ((x not in a) <= (x in R))):
#         a.append(x)
# print((a[-1]+1) - a[0])

# M = list(range(32, 69))
# N = list(range(54, 77))
# a = []
#
# for x in range(-100, 100):
#     if not(not((x in M) or (x in N)) == (not(x in a))):
#         a.append(x)
# print(a)
# print(len(a))
# print(a[-1]-a[0])

# def f(x, y):
#     return (x + y <= 30) or (y <= x + 2) or (y >= a)
# R = []
# for a in range(0, 1000):
#     if all(f(x, y) == 1 for x in range(1, 1000) for y in range(1, 1000)):
#         print(a)

# def f(x, y):
#     return (x+y <= 24) or (y <= x - 2) or (y >= a)
# for a in range(1, 1000):
#     if all(f(x, y) == 1 for x in range(1, 1000) for y in range(1, 1000)):
#         print(a)

# P = list(range(15, 41))
# Q = list(range(21, 64))
# a = []
# for x in range(-100, 100):
#     if not((x in P) <= (((x in Q) and (x not in a)) <= (x not in P))):
#         a.append(x)
# print(a)

# def f(x):
#     return (x % 12 == 0) <= (x % 42 != 0) or (x + a >= 4096)
# for a in range(1, 10000):
#     if all(f(x) == 1 for x in range(1, 1000)):
#         print(a)

# def f(x):
#     return (x % a == 0) or ((x % 133 == 0) <= (x % 95 != 0))
# for a in range(1, 1000):
#     if all(f(x) == 1 for x in range(1, 10**6)):
#         print(a)

# def f(x):
#     return (x & 47 == 0) or ((x & 13 == 0) <= (not(x & a == 0)))
# & - поразрядная конъюнкция
# for a in range(1, 10000):
#     if all(f(x) == 1 for x in range(1, 1000)):
#         print(a)
#         break

# P = list(range(2, 21, 2))
# Q = list(range(3, 31, 3))
# a = list(range(-100, 100))
# for x in range(-100, 100):
#     if not(((x in a) <= (x in P)) and ((x not in Q) <= (x not in a))):
#         a.remove(x)
# print(a)

# def f(x):
#     return (x & 79 != 0) and ((x & 31 == 0) <= (x & a != 0))
# for a in range(1, 1011):
#     if all(f(x) == 1 for x in range(90, 101)):
#         print(a)

# cnt = 0
# def f(x):
#     return ((a % x == 0) <= (x == a) or (x == 1))
# for a in range(1, 11112):
#     if all(f(x) == 1 for x in range(1, 11112)):
#         cnt += 1
# print(cnt)

# B = list(range(36, 75+1))
# C = list(range(60, 110+1))
# a = []
# for x in range(-100, 200):
#     if not((x not in a) <= ((x in B) == (x in C))):
#         print(x, end=" ")
# print()
# print(110-36)

# def F(x, y):
#     return (9*x + y > A) or (x >= 36) or (y >= 18)
# for A in range(1, 1000):
#     if all(F(x, y) == 1 for x in range(1, 1000) for y in range(1, 1000)):
#         print(A)

# def f(x):
#     B = list(range(70, 90+1))
#     return (x % A == 0) or ((x in B) <= (x % 22 != 0))
# for A in range(1, 1000+1):
#     if all(f(x) == 1 for x in range(1, 1000)):
#         print(A)

# def f(x):
#     return (x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0))
#
# for A in range(1, 1000+1):
#     if all(f(x) == 1 for x in range(1, 1000+1)):
#         print(A)

# def f(x, y, A):
#     return ((A < x) or (x**2 - 7*x + 10 > 0)) and ((A >= y) or (y**2 + 7 * y + 12 > 0))
# for A in range(-100, 100+1):
#     if all(f(x, y, A) == 1 for x in range(-100, 100+1) for y in range(-100, 100+1)):
#         print(A)

# def f(x, y, A):
#     return (x * y <= A + 13) <= (28 * y > 520) or (x * 25 > 800)
#
# for A in range(-100, 1000):
#     if all(f(x, y, A) == 1 for x in range(1, 1000) for y in range(1, 1000)):
#         print(A)

# def f(x):
#     return ((x & 17 != 0) <= ((x & A != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) and (x & A != 0) and (x & 58 == 0))
# for A in range(1, 1000):
#     if all(f(x) == 0 for x in range(1, 1000)):
#         print(A)


# B = list(range(60, 80+1))
# def f(x):
#     return (x % A == 0) or ((x in B) <= (x % 22 != 0))
#
# for A in range(1, 1000):
#     if all(f(x) == 1 for x in range(1, 1000)):
#         print(A)

# P = list(range(84, 341+1))
# Q = list(range(198, 412+1))
# A = []
# for x in range(-100, 500):
#     if (not((x in P) == (x in Q))) and (not(x in A)) == 1:
#         A.append(x)
# print(max(A) - min(A))

# def c(x, y):
#     return (x - 3 * y < A) or (y > 400) or (x > 56)
#
# for A in range(1, 10000):
#     if all(c(x, y) == 1 for x in range(1, 1000) for y in range(1, 1000)):
#         print(A)

# def c(x):
#     return ((x % 2 == 0) <= (x % 5 != 0)) or (x + A >= 70)
#
# for A in range(1, 1000):
#     if all(c(x) == 1 for x in range(1, 1000)):
#         print(A)


# B = list(range(60, 80+1))
# def c(x):
#     return (x % A == 0) or ((x in B) <= (x % 22 != 0))
#
# for A in range(1, 10000):
#     if all(c(x) == 1 for x in range(1, 10000)):
#         print(A)

# def c(x, y):
#     return (x > 67) or (y >= x) or ((3 * x - y) < A)
#
# for A in range(1,  1000):
#     if all(c(x, y) == 1 for x in range(0, 1000) for y in range(0, 1000)):
#         print(A)

# def f(x, y):
#     return (3 * x + y != 96) or (x <= y) or (A <= x)
#
# for A in range(1, 1000):
#     if all(f(x, y) == 1 for x in range(1, 1000) for y in range(1, 1000)):
#         print(A)


# def f(x, y):
#     return (x < A) and (y < 3 * A) or (2 * x + y > 128)
#
# for A in range(1, 1000):
#     if all(f(x, y) == 1 for x in range(1, 1000) for y in range(1, 1000)):
#         print(A)

# def f(x, y):
#     return (x < A) or (x*y > 50) or (x > y + 10)
#
# for A in range(1, 100):
#     if all(f(x, y) == 1 for x in range(1, 100) for y in range(1, 100)):
#         print(A)


