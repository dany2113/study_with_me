# region 📚 Шпаргалка ЕГЭ | Задание №16

# Задание №1:
# Алгоритм вычисления функции F(n) задан следующими соотношениями:
# (F(n) = 3) при (n ≤ 3)
# (F(n) = F(n // 2) + 5) при четных (n > 3)
# (F(n) = F(n - 1) - F(n - 2)) при нечетных (n > 3)
# Здесь «//» обозначает деление нацело. Определите значение, полученное при вызове F(20).

# Решение:
'''
def F(n):
    if n <= 3:
        return 3
    if n % 2 == 0 and n > 3:
        return F(n // 2) + 5
    if n % 2 != 0 and n > 3:
        return F(n - 1) - F(n - 2)

print(F(20))
'''
import string
import sys

# Задание №2:
# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
# F(n) = 2 при n < 3;
# F(n) = 2 × F(n − 2) − F(n − 1) + 2, если n > 2 и при этом n чётно;
# F(n) = 2 × F(n − 1) + F(n − 2) − 2, если n > 2 и при этом n нечётно.
# Чему равно значение функции F(170)?

# Решение (ускорение вычислений через библиотеку functools):
'''
from functools import *

@lru_cache(None)
def F(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return 2 * F(n - 2) - F(n - 1) + 2
    if n > 2 and n % 2 != 0:
        return 2 * F(n - 1) + F(n - 2) - 2

print(F(170))
'''

# Задание №3:
# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
# F(n) = 1, при n ≤ 7,
# F(n) = n + 2 + F(n − 1), если n > 7
# Чему равно значение выражения F(2024)−F(2020)?

# Решение (обход предела рекурсии через библиотеку sys)
'''
from sys import *

setrecursionlimit(10000)

def F(n):
    if n <= 7:
        return 1
    else:
        return n + 2 + F(n - 1)

print(F(2024) - F(2020))
'''

# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 16 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1609
# 💡 Кэширование через функцию @lru_cache(): https://t.me/informatika_kege_itpy/389
# endregion (не удаляйте меня, я тут не просто так)


# todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
# progress_result = ()  # Сюда заносятся номера, прорешанных задач.
# print('Рекомендуемое кол-во решенных задач для закрепления номера 30.')
# print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 30))}% задач прорешано.')

# своя теория:
#
# return сравни = (простая аналогия приравнивания для переменной)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# from sys import *
# sys.setrecursionlimit(10**6)
# def G(n):
#     if n <= 9:
#         return 3*n
#     if n > 9:
#         return G(n-2)+1
# def F(n):
#     return G(n - 1)
# print(F(47995))

# from sys import *
# sys.setrecursionlimit(10**6)
# def G(n):
#     if n < 10:
#         return 2*n
#     if n >= 10:
#         return G(n-2)+1
# def F(n):
#     return 2*(G(n-3)+8)
# print(F(15548))

# from sys import *
# sys.setrecursionlimit(10**7)
# def F(n):
#     if n <20:
#         return n
#     if n >= 20:
#         return (n-6)*F(n-7)
# print(((F(47872) - 290 * F(47865)))//F(47858))

# from functools import *
#
# @lru_cache(None)
# def f(n):
#     if n < 6: return n
#     return (3*n - 2) * f(n-5)
#
# for i in range(1, 21000): f(i) так как мы не задаём сам по себе лимит
# , что происходит при sys
# print((f(20568) - 51702 * f(20563))//f(20553))

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n < 13:
#         return 13
#     if n >= 13 and n % 5 != 0:
#         return 13-f(n-1)
#     if n >= 13 and n % 5 == 0:
#         return 13+f(n-1)
#
# for n in range(1, 3100): f(n)
# print(f(3013))

# from sys import *
# sys.setrecursionlimit(10**6)
# def f(n):
#     if n < 5: return n
#     if n >= 5:
#         return 2*n * f(n-4)
# print((f(13766) - 9*f(13762))//f(13758))

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n >= 2010: return n
#     return f(n+3) + f(n+2) + f(n+1)
# for n in range(1, 3000): f(n)
# print((f(2000) - 2 * (f(2002) + f(2003)))// f(2004))

# from functools import *
# @lru_cache(None)
# def G(n):
#     if n > 3:
#         return 6 * f(n-1) + 5 * G(n-1) + 3
#     if n == 3:
#         return 1
# def f(n):
#     if n == 3:
#         return 1
#     if n > 3:
#         return 5 * f(n-1)+6 * G(n-1) - 3*n + 8
#
# for n in range(1, 10): f(n), G(n)
# print(f(9) + G(9))

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n < 10: return n
#     return g(f(n-1)%10) + f(g(n%10)-1)-f(n-3)
# @lru_cache(None)
# def g(n):
#     if n < 10: return -n
#     return f(g(n-1)%10) + g(f(n-1)-1) + g(n-2)
#
# for n in range(1, 1300): f(n), g(n)
# print(f(1111)+g(1111))

# from functools import *
#
# @lru_cache(None)
# def f(n):
#     if n >= 2030: return n
#     return n + 2 + f(n+2)
# @lru_cache(None)
# def g(n):
#     if n <= 2030: return n
#     return n - 2 + g(n-2)
#
# print(g(2100)-f(2100))

# from functools import *
# cnt = 0
# @lru_cache(None)
# def f(n):
#     if n >1000000: return n
#     return n+f(n*2)
# @lru_cache(None)
# def g(n):
#     return f(n)//n
# for n in range(1000, 10**6+1):
#     if g(n) == g(2000):
#         cnt += 1
# print(cnt)

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n < 2025:
#         return n**2
#     if 2025 <= n < 2050:
#         return 2 * f(n-1) - f(n-2) + n
#     if 2050 <= n <= 2100:
#         return f(n-1) + 2 * f(n-2) + 3 * f(n-3)
#     if n > 2100:
#         return 2 * f(n-1) + f(n-2) + n
# for n in range(1, 2201): f(n)
# print(f(2020)+f(2200)%10**7)

# from functools import *
#
#
# @lru_cache(None)
# def f(n):
#     if n > 15: return n * 2
#     return 2 * f(n + 2) + 4 * n
# # if n == 1: return 3
# # return 4 * f(n-1) - 3 * n
# # if n < 2: return 1
# # return f(n - 1) * (n + 5)
# print(f(7))

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n == 1: return 1
#     if n % 2 == 0 and n > 1: return f(n - 1) + 7
#     if n % 2 != 0 and n > 1: return f(n - 2) + 4 * n
# print(f(100))

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n <= 4: return 0
#     if n % 4 == 0 and n > 4: return f(n - 1) + 3 * n
#     if n % 4 > 0 and n > 4: return f(n - (n % 4)) + 8 * n - 2
# print(f(43))

# from functools import *
#
#
# @lru_cache(None)
# def f(n):
#     if n == 2: return 1
#     if n > 2: return 3 * f(n - 1) + 4 * g(n - 1) - n * 2 + 4
#
#
# @lru_cache(None)
# def g(n):
#     if n == 2: return 1
#     if n > 2: return 4 * f(n - 1) + 3 * g(n - 1) + 6
#
#
# print(f(8), g(8), f(8) + g(8))
#
# from functools import *
# @lru_cache(None)
# def f(n):
#     if n == 1: return 1
#     if n > 1: return g(n - 1) + 3 * f(n - 1) - 5 * n + 1
# @lru_cache(None)
# def g(n):
#     if n == 1:
#         return 1
#     if n > 1: return 2 * f(n - 1) - g(n - 1) + 4 * n - 2
# print(g(12), f(12))
#
# from functools import *
#
#
# @lru_cache(None)
# def f(n):
#     if n < 11: return n
#     return n + f(n - 1)
#
#
# for n in range(2025): f(n)
# print(f(2024) - f(2021))

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n < 7: return 7
#     return n + 1 + f(n - 2)
# for n in range(2100): f(n)
# print(f(2024) - f(2020))

# from functools import *
#
# from sys import *
# sys.setrecursionlimit(10**6)
# def f(n):
#     if n == 1: return 1
#     if n > 1:
#         return 2 * n * f(n - 1)
# print((f(2024) - 4 * f(2023)) // f(2022))

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n == 1: return 1
#     if n > 1: return n * f(n - 1)
# for n in range(10000): f(n)
# print((2 * f(2024) + f(2023)) // f(2022))

# from functools import *
# from sys import *
# sys.setrecursionlimit(10**6)
# def f(n):
#     if n > 2024: return n
#     if n <= 2024: return n * f(n + 1)
# print(f(2022)//f(2024))

# from sys import *
# sys.setrecursionlimit(10**6)
# def f(n):
#     if n < 3: return 3
#     return 2 * n + 5 + f(n - 2)
# print(f(3027) - f(3023))

# from sys import *
# sys.setrecursionlimit(10**6)
# def f(n):
#     if n >= 3000: return n
#     return n + 5 + f(n + 2)
# print(f(108) - f(112))

# from sys import *
# sys.setrecursionlimit(10**6)
#
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1: return 2 * n * f(n - 1)
# print((f(2024) // 16 - f(2023)) // f(2022))

# from sys import *
# sys.setrecursionlimit(10**6)
#
# def f(n):
#     if n <= 3: return 2025
#     return 3 * (n - 1) * f(n - 2)
# print(f(2027) // f(2023))

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n == 1: return 6
#     if n > 1: return 3 * n + 2 + f(n - 1)
# for n in range(10000): f(n)
# print(f(2026) - f(2024))

# from functools import *
# @lru_cache(None)
# def f(n):
#     return g(n - 1) + g(n - 3)
# @lru_cache(None)
# def g(n):
#     if n <= 9: return 3 * n
#     return g(n-4) + 2
# for n in range(100000): f(n), g(n)
# print(f(42999))

# a = int(input())
# b = int(input())
# for i in range(a, b+1):
#     cnt = 0
#     if i <= 1:
#         continue
#     for n in range(1, b+1):
#         if i % n == 0:
#             cnt += 1
#         if cnt > 2:
#             break
#     if cnt == 2:
#         print(i)

# cnt = 0
# n = int(input())
# for i in range(1, n+1):
#     if n % i == 0:
#         cnt +=1
#     if cnt > 2 or n == 1:
#         print("Не простое число")
#         break
# else:
#     print("Простое число")

# срезы[start: step-1: stop]
# print(l[1:4])
# print(l[:4])
# print(l[1:])
# print(l[:]) - все элементы
# print(l[::-1]) - срез в обратном порядке
# print(l[::2]) -
# print(l[1::2]) - эелем под нечётными индексами

# функции списков
# len()
# sum() - сумму ЦЕЛЫХ чисел
# min()
# max()
# sorted() - сортирует список по возрастанию
# sorted(д, reverse=True) - сортирует список по убыванию
# set() - конвертация в множество (для убирания копий)

# методы
# .append() - добавляет
# .reverse() - переворачивает
# склеивание (как у строк)
# .count() - кол-во опред элем в списке
# .remove() - убирает первое вхождение в списке, указанное в условии
# del - удаляет элем по индексу
# .index/rindex (лучше со строками) - находит индекс элемента в условии/
# .sort - работает только со списками

# n = int(input())
# n1 = []
# for i in range(n):
#     n1.append(int(input()))
# n1.sort()
# print(n1[-2])

# n1 = []
# n = int(input())
# for i in range(n):
#     l = int(input())
#     if l % 2 == 0:
#         n1.append(l)
# print(n1)

# n1 = []
# n2 = []
# n = int(input())
# for i in range(n):
#     l = int(input())
#     if l % 2 != 0:
#         n1.append(l)
# print(n1)
# for i1 in n1:
#     if str(i1)[-1] != "5":
#         n2.append(i1**2)
# print(n2)

# n1 = []
# n = int(input())
# for i in range(n):
#     l = int(input())
#     if n < 0:
#         n1.append()
# n = 18812
# n = [int(x) for x in str(n)]
# cnt = 0
# cnt1 = 0
# cnt2 = 1
# print(n.count(2))
# print(n.count(n[-1]))
# for i in n:
#     if i % 2 != 0:
#         cnt += 1
# print(cnt)
# for i1 in n:
#     if i1 > 7:
#         cnt1 += i1
# print(cnt1)
# for i2 in n:
#     if i2 > 7:
#         cnt2 *= i2
#     else:
#         if n.count(i2 > 7) == 0:
#             cnt2 = 11
# print(cnt2)
# print(n.count(4)+n.count(0))

# from sys import *
# sys.setrecursionlimit(10**6)
# def f(n):
#     if n == 1: return 1
#     if n > 1: return n * f(n-1)
# print(f(1923)//f(1921)) 3696006

# from sys import *
# sys.setrecursionlimit(10**6)
# def f(n):
#     if n > 2024: return n
#     return n * f(n+1)
# print(f(2020)//f(2024))  16699163504520

# from sys import *
# sys.setrecursionlimit(10**6)
# def f(n):
#     if n == 1: return 1
#     if n > 1: return n + 1 + f(n-1)
# print(f(2024) + f(2020)) 4094552

# cnt = 0
# for n in range(1, 666+1):
#     def f(n):
#         if n <= 2: return (n*n)
#         if n % 2 == 0 and n > 2: return n + 7 * f(n - 2)
#         if n % 2 != 0 and n > 2: return 4 * n + f(n - 1)
#     if f(n) % 5 == 0:
#         cnt += 1
# print(cnt) 133

# cnt = 0
# for n in range(1, 300+1):
#     def f(n):
#         if n <= 3: return n
#         if n > 3 and n % 2 == 0: return n + 4 * f(n - 1)
#         if n > 3 and n % 2 != 0: return 2 * n**3 + f(n-1)
#     if f(n) % 6 == 0:
#         cnt += 1
# print(cnt) 98
from sys import *

# sys.setrecursionlimit(10**6)
# cnt = 0
# for n in range(1, 1300+1):
#     def f(n):
#         if n <= 4: return n**2
#         if n > 4 and n % 2 == 0: return n + 3* f(n-2)
#         if n > 4 and n % 2 != 0: return 2 * n + f(n-1)
#     if f(n) % 7 == 0:
#         cnt += 1
# print(cnt) 185

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n == 1: return 1
#     if n > 1: return 20 + f(n - 1) - g(n - 1) - 5 * n
# @lru_cache(None)
# def g(n):
#     if n == 1: return 1
#     if n > 1: return f(n-1) + 5 * g(n - 1) + 3 * n
# l = str(g(25))
# cnt1 = 0
# for i in l:
#     cnt1 += int(i)
# print(cnt1)

#
# from functools import *
#
# @lru_cache(None)
# def f(n):
#     if n == 1: return 1
#     if n >= 2: return f(n-1) + g(n - 1) + n * 2
# @lru_cache(None)
# def g(n):
#     if n == 1: return 1
#     if n >= 2: return f(n-1) + g(n-1) * 4
# for n in range(1, 100): f(n), g(n)
#
# print(f(50)//g(35)) 971295647

# from sys import *
# sys.setrecursionlimit(10**6)
#
# def f(n):
#     if n == 1: return 1
#     if n > 1: return n*f(n-1)
# print((3 * f(2025) + f(2024)) // f(2023))  12297824

# from sys import *
# sys.setrecursionlimit(10**6)
#
# def f(n):
#     if n == 1: return 1
#     if n > 1: return 3 * n * f(n-1)
# print((2 * f(2028) + f(2026)) // f(2024))  2732128919674650

# from functools import *
# @lru_cache(None)
# def f(n):
#     return 2 * (g(n-3) + 8)
# @lru_cache(None)
# def g(n):
#     if n < 10: return 2 * n
#     return g(n-2) + 1
# for n in range(1, 15600): f(n), g(n)
# print(f(15548))

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n < 6: return n
#     return (3*n - 2) * f(n - 5)
# for n in range(1, 21000): f(n)
# print((f(20568) - 51702 * f(20563)) // f(20553))

# for n in range(500):
#     def f(n):
#         if n < 15: return 4
#         if n >= 15 and n % 3 == 0: return f(2 * n // 3) + n - 1
#         if n >= 15 and n % 3 != 0: return f(n-1) + 3
#     if f(n) == 251:
#         print(n)

# from functools import *
#
# cnt = 0
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2 * n + f(n - 1)
#
#
# for n in range(58000):
#     f(n)
# l = str(f(57693))
# for i in l:
#     cnt += int(i)
# print(cnt**2)
# cnt = 0

# f = {}
# for k in range(1,  2* 10**12+1):
#     if k == 1:
#         f[k] = 1
#     if k > 1:
#         f[k] = (4*k + 7) * f[k - 1]
#     if k in range(10**12, 2*10**12+1) and f[k] % 2 == 0:
#         cnt += 1
# print(cnt)

# d = []
# n = int(input())
# for i in range(n):
#     l = int(input())
#     d.append(l**2)
# print(d)

# d = []
# n = input()
# for i in n:
#     d.append(int(i))
# l1 = max(d)
# f1 = min(d)
# l = d.index(max(d))
# f = d.index(min(d))
# d[l] = d[f]
# if d[f] != str(f1):
#     d[f] = l1
# s = ""
# for n in d:
#     s += str(n)
# print(s)

# d = [x for x in range(100, 1000) if str(x) == str(x)[::-1]]
# print(d)

# L = [-5, 6, 2, 7, -10, 4, 2, -2, -3]
# for i in range(len(L)):
#     if L[i] < 0:
#         L[i] = L[i]**2
# print(L)

# d = []
# n = int(input())
# for i in range(n):
#     l = int(input())
#     d.append(l)
# d.remove(max(d))
# d.remove(min(d))
# print(d)

# d = []
# n = int(input())
# for i in range(n):
#     l = int(input())
#     d.append(l)
# for i in range(len(d)-1):
#     b = d[i]+d[i+1]
#     print(b)

# d = []
# # n = int(input())
# # for i in range(1, n+1):
# #     if n % i == 0:
# #        d.append(i)
# # print(d)

# решение списком
# f = [0]*1000
# for n in range(1000):
#     if n < 2:
#         f[n] = 1
#     if n >= 2:
#         f[n] = f[n-1] * (n + 1)
#
# print(f[15])

# f = [0]*3000
# for n in range(3000):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n * f[n-1]
# print(f[2023]//f[2021])

# f = [0]*2100
# for n in range(2100):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n**3 + f[n-1]
# print(f[2024] - f[2020])

# f = [0] * 2100
# for n in range(2100):
#     if n == 1: f[n] = 1
#     if n == 2: f[n] = 2
#     if n > 2:
#         f[n] = (n - 1) * (n - 2) + f[n - 1] + f[n - 2]
# print(f[2021] - f[2019] - 2 * f[2018] - f[2017])

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n == 1: return 1
#     if n == 2: return 2
#     if n > 2: return (n - 1) * (n - 2) + f(n - 2)
# for n in range(2100): f(n)
# print(f(2021) - f(2019) - 2 * f(2018) - f(2017))

# f = [0]*10000
# for n in range(10000):
#     if n < 4 or n % 2 != 0:
#         f[n] = 1
#     if n > 3 and n % 2 == 0:
#         f[n] = f[n-1] + f[n-2] + f[n-3]
# print(f[4008] - f[4002])

# f = [0] * 100
# for n in range(100):
#     if n < 3: f[n] = 1
#     if n > 3: f[n] = f[n - 2] * (n // 3)
# print(f[16])


# f = [0]*2100
# for n in range(2100):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = (n-1) * f[n-1]
# print((f[2024] + 2 * f[2023]) // f[2022])

# f = [0]*5000
# for n in range(5000):
#     if n <= 3:
#         f[n] = n
#     if n > 3 and n % 2 == 0:
#         f[n] = f[n-2] + n//2 - f[n-4]
#     if n > 3 and n % 2 != 0:
#         f[n] = f[n-1] * n + f[n - 2]
# print(f[4952] + 2 * f[4958] + f[4964])

# f = [0]*800000
# for n in range(800000):
#     if n < 180:
#         f[n] = 24
#     if n >= 180:
#         f[n] = f[n - 12] + 6
# print(f[80000])

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n <= 3:
#         return n + 3
#     if n > 3:
#         return f(n-1) + 2 * f(n - 2) - f(n - 3)
# print(f(100))

# f = [0]*6000
# for n in range(6000):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = (4*n - 3) * f[n-1]
# print((f[5168]//11 + f[5166]) // f[5165])



# f = [0]*2000
# for n in range(2000):
#     if n < 2:
#         f[n] = 1
#     else:
#         f[n] = f[n-1] * (n+1)
# print(f[15])

# f = [0] * 2300
# for n in range(2300):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n * f[n-1]
# print(f[2023]//f[2021])

# f = [0]*2400
# for n in range(2400):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n**3 + f[n-1]
# print(f[2024] - f[2020])

# f = [0]*2200
# for n in range(2200):
#     if n == 1:
#         f[n] = 1
#     if n == 2:
#         f[n] = 2
#     if n > 2:
#         f[n] = (n - 1) * (n - 2) + f[n - 1] + f[n - 2]
# print(f[2021] - f[2019] - 2 * f[2018] - f[2017])

# f = [0] * 2000
# for n in range(20):
#     if n < 3:
#         f[n] = 1
#     if n > 3:
#         f[n] = f[n - 2] * (n // 3)
# print(f[16])

# f = [0]*4009
# for n in range(4009):
#     if n < 4 and n % 2 != 0:
#         f[n] = 1
#     if n > 3 and n % 2 == 0:
#         f[n] = f[n - 1] + f[n - 2] + f[n - 3]
# print(f[4008] - f[4002])

# def f(x):
#     if x <= 4:
#         return 0
#     if x > 4 and x % 4 == 0:
#         return f(x - 1) + 3 * x
#     if x > 4 and x % 4 > 0:
#         return f(x - (x % 4)) + 8 * x - 2
# print(f(43))

# f = [0]*100
# q = [0]*100
# for n in range(100):
#     if n == 1:
#         f[2] = 1
#         q[2] = 1
#     if n > 2:
#         f[n] = 3 * f[n - 1] + 4 * q[n - 1] - n * 2 + 4
#         q[n] = 4 * f[n - 1] + 3 * q[n - 1] + 6
# print(f[8] + q[8])

# def f(n):
#     if n > 1:
#         return f(n - 1) + (n - 1) * n
#     if n == 1:
#         return 3
# print(f(18))

# def f(n):
#     if n == 1:
#         return 2
#     if n > 1:
#         return 4 * f(n - 1) + 2 * n
# print(f(8))

# def f(n):
#     if n > 15:
#         return n - 2
#     if n < 15:
#         return 4 * f(n + 2) - 6
# print(f(6))

# def f(n):
#     if n < 4:
#         return 4 * n - 1
#     if n % 2 == 0 and n >= 4:
#         return f(n -2) + 2 * n
#     if n % 2 != 0 and n >= 4:
#         return f(n - 4) + 4 * n + 5
# print(f(62))

# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 3 == 0:
#         return f(n - 1) + 3 * n
#     if n > 0 and n % 3 > 0:
#         return f(n - (n % 3)) + 8 * n - 2
# print(f(30))

# f = [0]*14000
# for n in range(14000):
#     if n < 5:
#         f[n] = n
#     else:
#         f[n] = 2 * n * f[n - 4]
# print((f[13766] - 9 * f[13762]) // f[13758])

# f = [0]*2200
# for n in range(2200):
#     if n == 1:
#         f[n]=1
#     if n > 1:
#         f[n] = n**2 * f[n - 1]
# print((f[2024] + f[2023]) // f[2022])

# f = [0]*2200
# # for n in range(1, 2200):
# #     if n == 1:
# #         f[n] = 1
# #     if n > 1:
# #         f[n] = (n - 1) + 2 * f[n - 1]
# #
# # print((f[2024] + 2 * f[2023]) // f[2022])


# f = [0]*26000
# g = [0]*26000
# for n in range(26000):
#     f[n] = g[n-3]
#     if n <= 20:
#         g[n] = n
#     if n > 20:
#         g[n] = g[n - 2] + 1
# print(f[25000])

# f = [0]*3100
# for n in range(3100):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n * f[n - 1]
#
# print(((f[3000]//150) + f[2999])//f[2998])

# f = [0]*2000
# for n in range(2000):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n * f[n - 1]
# print(f[1923]//f[1921])

# f = [0]*2200
# for n in range(1, 2200):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = 2 * n + 3 * n * f[n - 1]
# print((2 * f[2024] + f[2023]) // f[2022])

# f = [0]*2100
# for n in range(2099, 1, -1):
#     if n > 2024:
#         f[n] = n
#     if n <= 2024:
#         f[n] = n * f[n + 1]
# print(f[2020]//f[2024])

# f = [0]*100
# g = [0]*100
# for n in range(1, 100):
#     g[1] = 1
#     f[1] = 1
#     if n > 1:
#         f[n] = 20 + f[n -1] - g[n - 1] - 5 * n
#         g[n] = f[n - 1] + 5 * g[n - 1] + 3 * n
# print(g[25])

# f = [0]*2100
# for n in range(1, 2100):
#     if n == 1: f[n] = 1
#     if n > 1: f[n] = n + 2 + f[n - 1]
# print(f[2028] + f[2022])

# f = [0]*3000
# for n in range(3000):
#     if n < 6: f[n] = n
#     if n >= 6: f[n] = f[n - 2] // 3 + 6 * n
# print((f[2765] + 3 * f[2763])//f[2759])

# f = [0]*2100
# for n in range(1, 2100):
#     if n == 122: f[n] = 156
#     if n > 1: f[n] = 2 * f[n - 1] + 4
# print(f[2017] - 4 * f[2015])

# f = [0]*3000
# for n in range(2999, 1, -1):
#     if n >= 2025: f[n] = n**2
#     if n < 2025: f[n] = f[n + 3] + n // 4
# print(f[2012] - f[2016])

# def f(n):
#     if n < 4: return n
#     if n >= 4: return f(n-1) + 5 * n**2
# print((f(776) + 7 * f(773)) / f(759))

# f = [0]*3100
# for n in range(1, 3100):
#     if n < 3: f[n] = 3
#     if n >= 3: f[n] = 2*n + 5 + f[n - 2]
# print(f[3027] - f[3023])

# f = [0]*2100
# for n in range(1, 2100):
#     if n <= 3: f[n] = 1
#     if n > 3: f[n] = (n + 3) * f[n - 2]
# print(f[2030] // f[2024])

# g = [0]*41000
# for n in range(1, 41000):
#     if n < 15:
#         g[n] = n
#     if n >= 15:
#         g[n] = (n - 8) * g[n - 6]
# print((g[40200] - 240 * g[40194]) // g[40188])

# f = [0]*43300
# g = [0]*43300
# for n in range(43300):
#     if n <= 9:
#         g[n] = 3*n
#     else:
#         g[n] = g[n - 4] + 2
#     f[n] = g[n - 1] + g[n - 3]
# print(f[42999])

# f = [0]*6000
# g = [0]*6000
# for n in range(6000):
#     if n < 100:
#         g[n] = n
#     f[n] = g[n-2]
#     if n >= 100:
#         g[n] = f[n - 3] + 1
# print(f[5000])
