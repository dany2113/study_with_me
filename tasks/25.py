
# region 📚 Шпаргалка ЕГЭ | Задание №25

# Задание №1:
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [174457;174505], числа,
# имеющие ровно два различных натуральных делителя, не считая единицы и самого числа.
# Для каждого найденного числа запишите эти два делителя в два соседних столбца на экране с новой строки
# в порядке возрастания произведения этих двух делителей.
# Делители в строке также должны следовать в порядке возрастания.

# Решение:
'''
d = Divisors(x) - находятся простые делители числа x.
if len(d) == 2: - проверяется, является ли количество простых делителей числа x равным 2 (само число и 1).
print(*d) - выводятся простые делители числа x, если число имеет ровно два простых делителя.
def Divisors(x):
    div = []
    for j in range(2, int(x ** 0.5) + 1):  # 2 - не считая единицы и самого числа.
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))

for x in range(174457, 174505 + 1):
    d = Divisors(x)
    if len(d) == 2:
        print(*d)
'''


# Задание №2:
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [95632;95650], числа,
# имеющие ровно шесть различных нечётных натуральных делителей (при этом количество четных делителей может быть любым).
# Для каждого найденного числа запишите эти шесть делителей в шесть соседних столбцов на экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.

# Решение:
'''
def Divisors(x):
    div = []
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))

for x in range(95632, 95650 + 1):
    d = Divisors(x)
    if len(d) == 6:
        print(*d)
'''


# Задание №3:
# назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# символ «?» означает ровно одну произвольную цифру;
# символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
# Среди натуральных чисел, не превышающих 10**9, найдите все числа,
# соответствующие маске 12345?7?8, делящиеся на число 23 без остатка.
#
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце — соответствующие им результаты деления этих чисел на 23.

# Решение:
'''
from fnmatch import *

for x in range(23, 10 ** 9, 23):
    if fnmatch(str(x), '12345?7?8'):
        print(x, x//23)
'''


# Задание №4:
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
#
# символ «?» означает ровно одну произвольную цифру;
# символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
# Например, маске 123*4?5 соответствуют числа 123405 и 12300425.
# Найдите все натуральные числа, не превосходящие 107, для которых выполняются одновременно все условия:
#
# – соответствуют маске *2?2*;
# – являются палиндромами;
# – делятся на число 53 без остатка;
# – количество делителей больше 30.
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце — сумму делителей.

# Решение:

# from fnmatch import *
#
# def divisors(x):
#     div = []
#     for j in range(1, int(x**0.5)+1):
#         if x % j == 0:
#             div += [j, x // j]
#     return sorted(set(div))
#
# for x in range(53, 10**7, 53):
#     if fnmatch(str(x), '*2?2*'):
#         if str(x) == str(x)[::-1]:
#             d = divisors(x)
#             if len(d) > 30:
#                 print(x, sum(d))



# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 25 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=2708
# 💡Циклы for и while, как использовать циклы для сдачи КЕГЭ: https://t.me/informatika_kege_itpy/169
# endregion (не удаляйте меня, я тут не просто так)

#
# # todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
# progress_result = ()  # Сюда заносятся номера, прорешанных задач.
# print('Рекомендуемое кол-во решенных задач для закрепления номера 50.')
# print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 50))}% задач прорешано.')


# from math import *
# def f(x):
#     delit = []
#     for i in range(2, isqrt(x)+1):
#         if x % i == 0:
#             delit += [i, x//i]
#     return sorted(set(delit))
#
# cnt = 0
# for x in range(300_000, 10**10):
#     l = 0
#     dev = f(x)
#     if len(dev):
#         for i in dev:
#             if i % 2 != 0:
#                 l += i
#     if l % 10 == 7:
#         cnt += 1
#         print(x, l)
#         if cnt == 5:
#             break

# from math import isqrt
# def f(x):
#     deliteli = []
#     for i in range(2, isqrt(x)+1):
#         if x % i == 0:
#             deliteli += [i, x // i]
#     return sorted(set(deliteli))
#
# cnt = 0
# for x in range(800_000, 10**10):
#     div = f(x)
#     if len(div):
#         M = max(div) + min(div)
#         if M % 10 == 4:
#             cnt += 1
#             print(x, M)
#         if cnt == 5:
#             break

# from fnmatch import *
# for x in range(84318, 10**12, 84318):
#     if fnmatch(str(x), "5*7?"):
#         if len(str(x)) == len(set(str(x))):
#             print(x, x // 84318)

#
# from math import isqrt
# def f(x):
#     deliteli = []
#     for i in range(1, isqrt(x)+1):
#         if x % i == 0:
#             deliteli += [i, x//i]
#     return deliteli
#
# cnt = 0
# for x in range(500_000, 10**12):
#     if cnt == 5: break
#     div = f(x)
#     R = sum(div)
#     if R % 10 == 6:
#         cnt += 1
#         print(x, R)

# from fnmatch import *
# for x in range(7993, 10**10+1, 7993):
#     if fnmatch(str(x), "4*4736*1"):
#         print(x, x // 7993)


# from math import  isqrt
# def f(x):
#     deliteli = sorted(set([]))
#     for i in range(2, isqrt(x)+1):
#         if x % i == 0:
#             deliteli += [i, x//i]
#     l = sorted([n for n in deliteli if n % 10 == 7 and n != x and n != 7])
#     return l
# cnt = 0
# for x in range(1_125_000, 10**10):
#     div = f(x)
#     if len(div):
#         cnt += 1
#         print(x, div[0])
#     if cnt == 5:
#         break

#
# from fnmatch import *
# for x in range(154682, 10**11, 154682):
#     if fnmatch(str(x), "*192?3*68"):
#         print(x, x//154682)

# from math import *
# def f(x):
#     deliteli = []
#     for i in range(2, isqrt(x)+1):
#         if x % i == 0:
#             deliteli += [i, x // i]
#     return deliteli
# cnt = 0
# for x in range(500_000, 10**12):
#     if cnt == 5: break
#     dev = f(x)
#     if len(dev):
#         R = sum(dev)
#         if R % 10 == 9:
#             cnt += 1
#             print(x, R)

# from math import *
# def f(x):
#     deliteli = []
#     for i in range(2, isqrt(x)+1):
#         if x % i == 0:
#             deliteli += [i, x // i]
#     l = sorted([n for n in deliteli if n % 10 == 5 and n != 5 and n != x])
#     return l
#
# cnt = 0
# for x in range(902714, 10**12):
#     if cnt == 6: break
#     div = f(x)
#     if len(div):
#         cnt += 1
#         print(x, div[0])

# from math import *
# def f(x):
#     deliteli = []
#     for i in range(2, isqrt(x)+1):
#         if x % i == 0:
#             deliteli += [i, x // i]
#     return sorted(set(deliteli))
# def Pr(x):
#     if x <= 1:
#         return False
#     for i in range(2, isqrt(x)+1):
#         if x % i == 0:
#             return False
#     return True
# cnt = 0
# for x in range(5_400_000, 10**12):
#     if cnt == 5: break
#     a = [n for n in f(x) if Pr(n) == True]
#     if len(a):
#         M = max(a) + min(a)
#         if M > 60000:
#             if str(M) == str(M)[::-1]:
#                 cnt += 1
#                 print(x, M)

# from math import *
# def Prost(x):
#     if x <= 1:
#         return False
#     for i in range(2, isqrt(x)+1):
#         if x % i == 0:
#             return False
#     return True
#
# def f(x):
#     deliteli = []
#     for i in range(2, isqrt(x)+1):
#         if x % i == 0:
#             deliteli += [i, x//i]
#     return deliteli
#
# cnt = 0
# for x in range(23_600_000, 10**10):
#     if cnt == 6: break
#     a = [j for j in f(x) if Prost(j) == True]
#     if len(a):
#         M = max(a) + min(a)
#         if M % 213 == 171:
#             cnt += 1
#             print(x, M)



