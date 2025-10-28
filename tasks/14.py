
# region 📚 Шпаргалка ЕГЭ | Задание №14

# Задание №1:
# Значение арифметического выражения 3 ∙ 625^173 + 4 ∙ 125^180 + 3 ∙ 25^157 + 2 ∙ 5^155 + 156
# записали в системе счисления с основанием 25.
# Сколько значащих нулей содержится в этой записи?

# Решение:
'''
def my_convert(number: int, system: int) -> str:
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    result = ''
    while number > 0:
        result += alphabet[number % system]
        number //= system
    return result[::-1]

x = 3 * 625 ** 173 + 4 * 125 ** 180 + 3 * 25 ** 157 + 2 * 5 ** 155 + 156
s = my_convert(x, 25)
print(s.count('0'))
'''
import string

# Задание №2:
# Операнды арифметического выражения записаны в системе счисления с основанием 15.
#
# 1x51_15 − 3x2_15
#
# В записи чисел переменной x обозначена неизвестная цифра из алфавита 15-ричной системы счисления.
# Определите наибольшее значение x, при котором значение данного выражения кратно 4.
# Для найденного x вычислите частное от деления данного выражения на 4 и запишите его
# в ответе в десятичной системе счисления. Основание системы счисления указывать не нужно.

# Решение:
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
M = []
for x in alphabet[:15]:
    A = int(f'1{x}51', 15)
    B = int(f'3{x}2', 15)
    if (A - B) % 4 == 0:
        M.append((A - B) // 4)
print(max(M))
'''


# Задание №3:
# Операнды арифметического выражения записаны в системах счисления с основаниями 9 и 8:
#
# x01y4_9 + xy544_8
#
# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 89.
# Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 89
# и укажите его в ответе в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно.

# Решение:
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
M = []
for x in alphabet[:8]:
    for y in alphabet[:8]:
        A = int(f'{x}01{y}4', 9)
        B = int(f'{x}{y}544', 8)
        if (A + B) % 89 == 0:
            M.append((A + B) // 89)
print(min(M))
'''


# Задание №4:
# В системе счисления с основанием p выполняется равенство 24x9_p + yxy3_p = x4y0_p.
# Буквами x и y обозначены некоторые цифры из алфавита системы счисления с основанием p.
# Определите значение числа xyy_p и запишите это значение в десятичной системе счисления.

# Решение:
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(10, 36 + 1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            if int(f'24{x}9', p) + int(f'{y}{x}{y}3', p) == int(f'{x}4{y}0', p):
                print(int(x + y + y, p))
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 14 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1535
# 💡Условные операторы if, else, elif а также логические операторы and и or: https://t.me/informatika_kege_itpy/294
# 💡Срезы, что это такое и где могут пригодиться на ЕГЭ: https://t.me/informatika_kege_itpy/351
# endregion (не удаляйте меня, я тут не просто так)


# todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
# progress_result = ()  # Сюда заносятся номера, прорешанных задач.
# print('Рекомендуемое кол-во решенных задач для закрепления номера 50.')
# print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 50))}% задач прорешано.')

# print(bin(16**16+8**8+32**4)[2:].count("1"))
# print(bin(16**16+8**8+32**4)[2:])
# print(bin(16**16+8**8+32**4)) ans 3

# print(oct(4096**8 + 512**64 - 64**512)[2:].count("7")) ans 991

# print(bin(1234**1234 + 123**123 - 12**12)[2:].count("1")) ans 6217

# print(bin(1111**111 + 111**11 - 11)[2:].count("0")) ans 556

# def c4(x):
#     s = ""
#     while x > 0:
#        s = str(x%4) + s
#        x //= 4
#     return s
# print(c4(234**123 + 32**12 - 32).count("3")) ans 136

# def c5(x):
#     s = ""
#     while x > 0:
#         s = str(x%5) + s
#         x //= 4
#     return s
# print(c5(125**27 * 625**81 + 25**9 - 5).count("4")) ans 77

# for x in range(3, 37):
#     if int("222", x) + int("17", 8) == int("238", 9):
#         print(x) ans 9

# p = "0123456789ABCDEFGH"
# for n in p:
#     if (int(f"AB5{n}3", 18) + int(f"EF{n}13", 18)) % 17 == 0:
#         print((int(f"AB5{n}3", 18) + int(f"EF{n}13", 18)) // 17)

# for x in range(7, 37):
#     if int("165", x) + int("18", 9) == int("416", 7):
#         print(x)
#         break

# def c5(x):
#     s = ""
#     while x > 0:
#         s = str(x%5)+s
#         x //= 5
#     return s
#
# print(c5(1024**789 + 256**678 - 64**567).count("4"))

# print(oct(4096**3125 - 512**625 + 64**125 - 8**25)[2:].count("7"))

# print(bin(64**13 + 32**6 - 16**2)[2:].count("1"))

# def c9(x):
#     s= ""
#     while x > 0:
#         s = str(x%9)+s
#         x //= 9
#     return s
#
# n = c9(9**2024 + 7 * 9**1000 + 9**1012 + 7 * 9**250 + 2)
# print(n.count("0")) ans 2020

# n = bin(64**2023 + 32**2022 - 8**2021 - 2)[2:]
# n1 = n.count("1")
# print(hex(n1)) ans 277d

# def c20(x):
#     s = ""
#     while x > 0:
#         s = str(x%20)+s
#         x //= 20
#     return s
# n1 = []
# n = c20(64**2023 + 32**2022 - 8**2021 - 2)
# for i in n:
#     n1.append(i)
#     sorted(n1)
# print(sorted(set(n1))) ans 10

# for N in range(3, 32):
#     if int("121", N+1) == int("121", N) + int("13", 16):
#         print(N) ans 8

# import string
# alfavet = "0123456789ABCDEF"
# for x in alfavet:
#     if int((int(f"D491"+x+"1", 16) + int("48A3"+x, 16))) % 14 == 0:
#         print(int((int(f"D491"+x+"1", 16) + int("48A3"+x, 16))) // 14) ans 1016321

# import string
# alf = "0123456789ABCDEFGHIJKLMNOPQRST"
# for x in alf:
#     if (int("39"+x+"9"+x+"DE", 30) + int(x[1:]+"M13F", 30) + int("11"+x+"9", 30)) % 17 == 0:
#        print(x, (int("39"+x+"9"+x+"DE", 30) + int(x[1:]+"M13F", 30) + int("11"+x+"9", 30)) // 17)
# and B 142087444
#
# n = 127342 + 399340 - 29**3
# s = []
# while n > 0:
#     n % 15
#     if n % 15 >= 10:
#         s.append(n%15)
#     n //= 15
# print(s)

# for x in range(0, 38):
#     n = (1*37**4 + 7*37**3+ 2*37**2+ 1*37**1 + x*37**0) + (2*37**5 + 5*37**4 + x*37**3 + 3*37**2 + 4*37**1 + x*37**0)
#     if n % 13 == 0:
#         print(x, n // 13)
#         break

# n1 = []
# n2 = []
# n3 = []
# for c in range(0, 37):
#     for d in range(0,37):
#         n = (4*37**6 + 5*37**5 + c*37**4 + 7*37**3 + 3*37**2 + d*37**1 + 9*37**0)
#         if n % 15 == 0:
#             print(c*37 + d)

# cnt = 0
# n = 3 * 5103**2020 + 3 * 729**2021 - 2 * 343**2022 + 27**2023 - 4 * 7**2024 - 2029
# if n % 36 > 12:
#     cnt += 1
#     n // 36
# print(cnt)

# def c9(x):
#     s = ""
#     while x > 0:
#         s = str(x%9) +s
#         x //= 9
#     return s
#
# for x in range(0, 2401):
#     n = c9(7*9**210 +6*9**110 -x)
#     if n.count("0") == 100:
#         print(x)

# for x in range(0, 21):
#     n = int("82934"+str(x)+"2", 21) + int("2924"+str(x)+str(x)+"7", 21) + int("67564"+str(x)+"8", 21)
#     if n % 20 == 0:
#         print(x, n//20)

# def c5(x):
#     s = ""
#     while x > 0:
#         s = str(x%5)+s
#         x //= 5
#     return s
# l = 0
# for x in range(1, 2006):
#     n = c5(5**150 + 5**98 - x)
#     k = n.count("0")
#     if k >= l:
#         l = k
#         print(x, l)

# def c4(x):
#     s =""
#     while x > 0:
#         s = str(x%4)+s
#         x //= 4
#     return s
#
# n1 = []
# n2 = []
# n3 = []
# for x in range(1, 2006):
#     n = c4(43**56+ 113**841 - x)
#     for i in n:
#         if int(i) % 2 == 0:
#             n1.append(i)
#         elif int(i) % 2 != 0:
#             n2.append(i)
#     if n.count("2") == 712 and len(n1) % 2 == 0 and len(n2) % 2 == 0:
#         print(x)

# for x in range(0, 15):
#     M = int("432"+str(x)+"3", 15)
#     N = int("86"+str(x)+"86", 15)
#     for A in range(1, 1000000):
#         if (M + A) % N == 0:
#             print(x, A)

# for p1 in range(30, 37):
#     for s in range(20, 35):
#         if int("R4", p1-1) + int("B0", s + 2) + int("T3NK4", p1) == 23593399:
#             print(p1*s)
#             break

# def c6(x):
#     s = ""
#     while x > 0:
#         s = str(x%6)+s
#         x//=6
#     return s
#
# for x in range(1, 10001):
#     n = c6(6**900+6**10-x)
#     if n.count("3") == n.count("5"):
#         print(x)

# cnt = 0
# n = 17*125**453 + 117 * 5**231 - 3 * 5**13 - 2357
# while n > 0:
#     if n % 125 <= 37:
#         cnt += 1
#     n //= 125
# print(cnt)

# from string import *
# a = "0123456789ABCDEFGHIJKLMNOPQRS"
# for x in a:
#     n = int("463"+str(x)+"7921", 29) + int("8241"+str(x)+"153", 29)
#     if n % 28 == 0:
#         print(x, n//28)


# def c5(x):
#     s =""
#     while x > 0:
#         s = str(x%5)+s
#         x//=5
#     return s
#
# for x in range(1, 2006):
#     n = c5(5**150 + 5**98 - x)
#     if n.count("0") > 54:
#         print(x, n.count("0"))

# def c7(x):
#     s = ""
#     while x > 0:
#         s = str(x % 7) + s
#         x //= 7
#     return s
# maxi = -1000
# c = 0
# for x in range(1, 2030+1):
#     p = c7(7**170 + 7**100 - x)
#     l = p.count("0")
#     if l > maxi:
#         maxi = l
#     if l > 72:
#         print(x, maxi, l)


# for p in range(30, 36+1):
#     for s in range(10, 34+1):
#         if int("R4", p-1) + int("B0", s + 2) + int("T3NK4", p) == 23593399:
#             print(p, s)

# alf = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")
# for p in range(10, 36+1):
#     for x in alf[:p]:
#         for y in alf[:p]:  g
#             A = int(f"24{x}9", p)
#             B = int(f"{y}{x}{y}3", p)
#             C = int(f"{x}4{y}0", p)
#             if A + B == C:
#                 print(int(f"{x}{y}{y}", p))

# alf = sorted("0123456789AB")
# for x in alf:
#     for y in alf:
#         A = int(f"{x}231{y}", 12)
#         B = int(f"78{x}98{y}", 14)
#         if (A + B) % 99 == 0:
#             print(x, y, (A + B) // 99)
# alf = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")
# def c(x, b):
#     s = ""
#     while x > 0:
#         s = alf[x % b] + s
#         x //= b
#     return s
#
# k = c(3 * 3125**9 + 2 * 625**8 - 4 * 625**7 + 3 * 125**6 - 2 * 25**5 - 2024, 25)
# print(k.count("0"))
# print(k)
# print(len(k) - k.count("0"))
# print(len([x for x in k if x > "9"]))
# print(sorted("agdhajkasAGHJKALK1234"))

# alf = "0123456789A"
# def c(x, y):
#     s = ""
#     while x > 0:
#         s = alf[x % y] + s
#         x //= y
#     return s
#
# k = []
# for x in range(1, 3000+1):
#     n = c(9 * 11**210 + 8 * 11**150 - x, 11)
#     if n.count("0") == 60:
#         k.append(x)
# print(max(k))

#
# alf = sorted("0123456789QWERTYIOPASDFGHJKLZXCVBNM")
# def c(x, b):
#     s = ""
#     while x > 0:
#         s = alf[x % b] + s
#         x //= b
#     return s
#
# n = c(11*15**65+18*15**38-14*15**17+19*15**11+18338, 15)
# print(len(set(n)))

# alf = "0123456789ABCDE"
# a = []
# for x in alf:
#     A = int(f"1{x}51", 15)
#     B = int(f"3{x}2", 15)
#     if (A - B) % 4 == 0:
#         a.append((A - B) // 4)
# print(max(a))

# alf = "0123456"
#
# for x in alf:
#     for y in alf:
#         A = int(f"{y}{x}320", 7)
#         B = int(f"1{x}3{y}3", 9)
#         if (A + B) % 181 == 0:
#             print((A + B) // 181)
#             break

# alf = sorted("012345")
# def c(x, b):
#     s =""
#     while x > 0:
#         s=  alf[x % b] + s
#         x //= b
#     return s
#
# for x in range(1, 2030+1):
#     n = c(6**260 + 6**120 + 6**60 - x, 6)
#     if n.count("0") == 202:
#         print(x)
#         break

# alf = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")
# def c(x, y):
#     s = ""
#     while x > 0:
#         s = alf[x % y] + s
#         x //= y
#     return s
#
# n = 766**66 + 15**13 - 22
# b = c(n, 13)
# print(b.count("C"))

# alf = "0123456789ABCDE"
# for x in alf:
#     a = int(f"97531{x}19", 15)
#     b = int(f"3{x}519", 15)
#     if (a + b) % 11 == 0:
#         print((a + b) // 11)
#         break

# alf = "0123456789ABCDE"
# alf1 = "0123456789ABCDEF"
# l = []
# for x in alf:
#     for y in alf1:
#         a = int(f"123{x}5", 15)
#         b = int(f"67{y}9", 17)
#         if (a + b) % 131 == 0:
#             l.append((a + b) // 131)
# print(l[-1])

# alf = sorted("0123456789QERTYUIOPASDFGHJKLZXCVBNM")
# l  =[]
# for x in alf[:18]:
#     a = int(f"77968{x}11", 18)
#     b = int(f"4{x}213", 18)
#     if (a + b) % 7 == 0:
#         l.append((a + b) // 7)
# print(max(l))

# alf = "012"
# def c(x, b):
#     s = ""
#     while x > 0:
#         s = alf[x % b] + s
#         x //= b
#     return s
#
# l = []
# for x in range(1, 2030+1):
#     n = c(3**100 - x, 3)
#     if n.count("0") == 5:
#         l.append(x)
# print(max(l))

# alf = "01234567"
# for x in alf:
#     for y in alf:
#         a = int(f"{y}04{x}5", 11)
#         b = int(f"253{x}{y}", 8)
#         if (a + b) % 117 == 0:
#             print((a + b) // 117)
#             break

# def c(x):
#     s = ""
#     while x > 0:
#         s = str(x % 7) + s
#         x //= 7
#     return s
#
# l = []
# for x in range(1, 2030+1):
#     n = c(7**91 + 7**160 - x)
#     if n.count("0") == 70:
#         l.append(x)
# print(max(l))


# for p in range(5, 36+1):
#     for q in range(6, 36+1):
#         if int("234", p) == int("345", q):
#             print(int("234", p))

# alf = sorted("0123456789ABCDEF")
# for x in alf:
#     a = int(f"1F3B{x}75", 16)
#     b = int(f"5D{x}3B", 16)
#     if (a + b) % 11 == 0:
#         print((a + b) // 11)

# def c6(x):
#     s = ""
#     while x > 0:
#         s = str(x % 6) + s
#         x //= 6
#     return s
#
# for x in range(1, 2030+1):
#     n = c6(6**260 + 6**160 + 6**60 - x)
#     if n.count("0") == 202:
#         print(x)
#         break

# for n in range(6, 36+1):
#     if (7**500 - int("53", n)) % 6 == 0:
#         print(n)
#         break

# alf = "0123456789ABC"
# l = []
# for x in alf:
#     A = int(f"537{x}623", 13)
#     B = int(f"6{x}35{x}2", 13)
#     if (A - B) % 3 == 0:
#         l.append(int(f"{x}", 13))
# print(max(l))

# def c7(x):
#     s = ""
#     while x > 0:
#         s = str(x % 7) + s
#         x //= 7
#     return s
#
#
# l = []
# for x in range(1, 2030 + 1):
#     n = c7(7**91 + 7**160 - x)
#     if n.count("0") == 70:
#         l.append(x)
# print(max(l))

# def c25(x):
#     s = ""
#     while x > 0:
#         s = str(x % 25) + s
#         x //= 25
#     return s
#
# n = c25(3 * 3125**9 + 2 * 625**8 - 4 * 625**7 + 3 * 125**6 - 2 * 25**5 - 2024)

#
# alf = sorted("0123456789QWWERTYUIOPASDFGHJZKLXCVBNM")
# for x in alf[:26]:
#     a = int(f"27{x}98876", 26)
#     b = int(f"26{x}51", 26)
#     v = int(f"15{x}47", 26)
#     d = int(f"62{x}5", 26)
#     if (a + b + v + d) % 25 == 0:
#         print((a + b + v + d) // 25)
#         break

# from string import ascii_uppercase
# s = ascii_uppercase
# alf = ("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# l = []
# for x in alf[:27]:
#     a = int(f"17{x}35", 27)
#     b = int(f"{x}742M", 27)
#     c = int(f"{x}", 27)**3
#     if (a + b + c) % 23 == 0:
#         l.append((a + b + c) // 23)
# print(max(l))

# alf = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for x in alf[:32]:
#     a = int(f"931{x}964", 32)
#     b = int(f"4{x}51{x}1", 32)
#     v = int(f"2861{x}637", 32)
#     if (a + b + v) % 31 == 0:
#         print((a + b + v) // 31)
#         break

# alf = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")
# for p in range(5, 36+1):
#     for x in alf[:p]:
#         for y in alf[:p]:
#             if int("32", p) * int("14", p) == int(f"{x}{y}2", p):
#                 print(int(f"{y}{x}", p))

# def c9(x):
#     s = ""
#     while x > 0:
#         s = str(x % 9) + s
#         x //= 9
#     return s
#
# for x in range(1, 2024+1):
#     n = c9(9**2024 + 9**1987 - x)
#     if n.count("8") == 1984:
#         print(x)

# def c4(x):
# #     s = ""
# #     while x > 0:
# #         s = str(x % 4) + s
# #         x //= 4
# #     return s
# # maxi = -1
# # for x in range(1, 3000+1):
# #     n = c4(4**210 + 4**110 - x)
# #     if n.count("0") >= 105:
# #         print(x)

# from string import ascii_uppercase
# alf = "0123456789" + ascii_uppercase
# print(alf[:27])
# def c(x, b):
#     s = ""
#     while x > 0:
#         s = alf[x % b] + s
#         x //= b
#     return s
#
# cnt = 0
# n = c(4 * 729**2025 + 2 * 243**1413 - 5 * 81**169 - 3 * 9**107 + 7019, 27)
# print(n)
# print(n.count("Q"))
# print(n.count("I"))
#
# from string import ascii_uppercase
# alf = "0123456789" + ascii_uppercase
# def c(x, b):
#     s = ""
#     while x > 0:
#         s = alf[x % b] + s
#         x //= b
#     return s
# chis = []
# n = c(5 * 729**2024 + 3 * 243**1413 - 7 * 81**169 - 2 * 9**107 + 3017, 27)
# for i in n:
#     if int(i, 27) <= 25:
#         chis.append(int(i, 27))
# print(sum(chis))


# def c(x):
#     s = ""
#     while x > 0:
#         s = str(x % 7) + s
#         x //= 7
#     return s
# cnt = 0
# l = []
# for x in range(1, 3000+1):
#     n = c(5 * 7**156 + 3 * 7**10 - x**31)
#     if n.count("0") == 15:
#         cnt += 1
#         l.append(x)
# print(cnt)
# print(len(l))

# for x in sorted("123456789QWERTYUIOPASDFGHJKLZXCVBNM")[:20]:
#     a = int(f"{x}5B{x}8", 21)
#     b = int(f"H053{x}7", 21)
#     if (a + b) % 12 == 0:
#         print((a + b) // 12)

# m = bin(64**13 + 32**6 - 16**2)[2:]
# print(m.count("1"))

# m = oct(4096**3125 - 512**625 + 64**125 - 8**25)[2:]
# print(m.count("7"))

# def c5(x):
#     s = ""
#     while x > 0:
#         s = str(x % 6) + s
#         x //= 6
#     return s
#
# n = c5(1296**625 * 216**125 + 36**25 - 6**5)
# print(n.count("5"))

#
# for x in range(7, 25+1):
#     if int("165", x) + int("18", 9) == int("416", 7):
#         print(x)

# from string import ascii_uppercase
# alf = ("0123456789" + ascii_uppercase)
# for x in alf[:18]:
#     a = int(f"AB5{x}3", 18)
#     b = int(f"EF{x}13", 18)
#     if (a + b) % 17 == 0:
#         print((a + b) // 17)


# from string import  ascii_uppercase
# alf = ("0123456789" + ascii_uppercase)
# for x in alf[:25]:
#     a = int(f"11353{x}12", 25)
#     b = int(f"135{x}21", 25)
#     if (a + b) % 24 == 0:
#         print((a + b) // 24)

# from string import *
# alf = ("0123456789" + ascii_uppercase)[:17]
# for x in alf:
#     A = int(f"18{x}AE", 17)
#     b = int(f"733{x}C", 17)
#     if (A + b) % 13 == 0:
#         print((A + b) // 13)

# def c7(x):
#     s = ""
#     while x > 0:
#         s = str(x % 7) + s
#         x //= 7
#     return s
# #
# k = -1
# for x in range(1, 2030+1):
#     n = c7(7**170 + 7**100 - x)
#     if n.count("0") >= k:
#         k = n.count("0")
#         print(k, x)
#
# from string import *
# alf = ("0123456789" + ascii_uppercase)[:30]
# for x in alf:
#     A = int(f"7{x}A9F", 30)
#     B = int(f"1B3{x}", 30)
#     if (A + B) % 29 == 0:
#         print((A + B) // 29)


# from string import  ascii_uppercase
#
# alf = "0123456789" + ascii_uppercase
#
# for x in alf[:32]:
#     A = int(f"54{x}45", 32)
#     B = int(f"96{x}", 32)
#     C = int(f"12{x}1", 32)
#     if (A + B * C) % 8 == 0:
#         l = int(x, 32)
#         print(bin(l)[2:])