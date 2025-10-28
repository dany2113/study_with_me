
# region 📚 Шпаргалка ЕГЭ | Задание №8

# Задание №1:
# Все шестибуквенные слова, в составе которых могут быть только русские буквы А, Е, К, Н, С записаны
# в алфавитном порядке и пронумерованы начиная с 1.
# Ниже приведено начало списка.
#
# АААААА
# АААААЕ
# АААААК
# АААААН
# АААААС
# ААААЕА
# Под каким номером в списке идёт слово СЕНЕКА?

# Решение (через itertools):
'''
import itertools
count = 0
for s in itertools.product('АЕКНС', repeat=6):
    slovo = ''.join(s)
    count += 1
    if slovo == 'СЕНЕКА':
        print(count)
'''

# Решение (через цикл for):
'''
s = 'АЕКНС'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        count += 1
                        if slovo == 'СЕНЕКА':
                            print(count)
'''


# Задание №2:
# Ярослав составляет коды из букв, входящих в слово ЯРОСЛАВ.
# Код должен состоять из 5 букв,
# буквы в коде не должны повторяться, согласных в коде должно быть больше, чем гласных,
# две гласные буквы нельзя ставить рядом.
# Сколько кодов может составить Ярослав?

# Решение (через itertools):
'''
import itertools
count = 0
for s in itertools.permutations('ЯРОСЛАВ', 5):
    slovo = ''.join(s)
    glas = [i for i in slovo if i in 'ЯОА']
    sogl = [i for i in slovo if i in 'РСЛВ']
    if len(sogl) > len(glas):
        if all(x not in slovo for x in 'ЯА АЯ АО ОА ЯО ОЯ'.split()):
            count += 1
print(count)
'''

# Решение (через цикл for):
'''
s = 'ЯРОСЛАВ'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if len(set(slovo)) == 5:
                        glas = [i for i in slovo if i in 'ЯОА']
                        sogl = [i for i in slovo if i in 'РСЛВ']
                        if len(sogl) > len(glas):
                            if all(x not in slovo for x in 'ЯА АЯ АО ОА ЯО ОЯ'.split()):
                                count += 1
print(count)
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 8 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1471
# 💡 Функции split() и join(), где они могут пригодиться на КЕГЭ: https://t.me/informatika_kege_itpy/126
# 💡 Функции all() и any(), где они могут пригодиться на ЕГЭ: https://t.me/informatika_kege_itpy/378
# 🐍 Функция permutations() из библиотеки itertools в Python: https://t.me/informatika_kege_itpy/391
# 🐍 Функция product из библиотеки itertools в Python: https://t.me/informatika_kege_itpy/393
# 🐍 Вспомним полезные функции из библиотеки itertools: https://t.me/informatika_kege_itpy/470
# endregion (не удаляйте меня, я тут не просто так)


# # todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
# progress_result = ()  # Сюда заносятся номера, прорешанных задач.
# print('Рекомендуемое кол-во решенных задач для закрепления номера 50.')
# print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 50))}% задач прорешано.')


# from itertools import *
# p = sorted("ТЕОРИЯ")
# k = 0
# for i in product(p, repeat=6):
#     i = "".join(i)
#     k += 1
#     if k % 2 != 0 and i[0] not in "РТЯ" and i.count("И") >= 2:
#         print(i, k)

# from itertools import *
# p = sorted("Фокус")
# k = 0
# for s in product(p, repeat=5):
#     s = "".join(s)
#     k += 1
#     if "Ф" not in s and s.count("у")== 2:
#         print(s, k)


# from itertools import *
# cnt = 0
# p = "BLANK"
# for s in product(p, repeat= 6):
#     s = "".join(s)
#     if s.count("N") == 2 and s[0] == "K":
#         cnt += 1
# print(cnt)

# from itertools import *
# cnt = 0
# p = "0123456"
# k = "0246"
# for s in product(p, repeat = 5):
#     s = "".join(s)
#     if s.count("4") == 1 and s[-1] not in k and s[0] != "0":
#         cnt += 1
#         print(s, cnt)

# from itertools import *
# cnt = 0
# p = "01234"
# for s in product(p, repeat = 5):
#     s = "".join(s)
#     if s.count("4") == 1 and "42" not in s and "24" not in s and s[0] != "0":
#         cnt += 1
# print(cnt)

# from itertools import *
# cnt = 0
# p = "01234567"
# cht = "0246"
# for s in product(p, repeat = 5):
#     s = "".join(s)
#     if s[0] not in cht and (s[-1] not in "27") and s.count("3") <= 1:
#         cnt += 1
#         print(s, cnt)


# from itertools import *
# cnt  = 0
# p = "ФОРМАТ"
# for s in set(permutations(p, r = 5)):
#     s= "".join(s)
#     if s[0] != "А" and s.count("Р") == 1:
#         cnt += 1
# print(cnt)

# from itertools import *
# cnt = 0
# p = "MEDIA"
# for s in permutations(p, r = 5):
#     s = "".join(s)
#     if s[0] != "A" and "EDA" not in s:
#         cnt += 1
#         print(s, cnt)

# from itertools import *
# cnt = 0
# p = "PIKSELO"
# for s in permutations(p, r = 7):
#     s = "".join(s)
#     if s[0] != "O" and "OIE" not in s:
#         cnt += 1
# print(cnt)

# from itertools import *
# cnt = 0
# p = "TARA"
# for s in set(permutations(p, r = 4)):
#     s = "".join(s)
#     if "AA" not in s:
#         cnt += 1
#         print(s, cnt)

# from itertools import *
#
# p = "0123"
# cnt = 0
# for s in permutations(p, r=3):
#     s = "".join(s)
#     if (int(s[0]) > int(s[1])) and (int(s[1]) > int(s[2])):
#         cnt += 1
#         print(s, cnt)

# from itertools import *
# p = "0123456789"
# cnt = 0
# for s in product(p, repeat = 5):
#     s = "".join(s)
#     if s.count("2") >= 1 or s.count("3") >= 1:
#         cnt += 1
# print(cnt)

# from itertools import *
# p = sorted("AKORST")
# cnt = 0
# for s in product(p, repeat=5):
#     s = "".join(s)
#     cnt += 1
#     if cnt % 2 == 0 and s[0] not in "AST" and s.count("O") == 2:
#         print(cnt)

# from itertools import *
# cnt = 0
# for s in product("AKMS", repeat = 6):
#     s = "".join(s)
#     cnt += 1
#     if s.count("S") == 0 and s.count("M") == 0 and "KK" not in s:
#         print(cnt)

# cnt = 0
# for s in range(100000, 1000000):
#     s = str(s)
#     cnt += 1
#     if str(cnt)[-1] == "5":
#         print(s, cnt)

# from itertools import *
# cnt  =0
# for s in product("АКОРСТ", repeat = 5):
#     s = "".join(s)
#     cnt += 1
#     if s.count("С") == 1 and s[0] not in "АЛ" and cnt % 2 != 0:
#         print(cnt)

# from itertools import *
# cnt = 0
# for s in product("ДИОНСЙ", repeat = 6):
#     s = "".join(s)
#     if ("Д" in s) + ("Н" in s) == 1:
#         if all(s[i] != s[i+1] for i in range(0, len(s)-1)):
#             cnt += 1
# print(cnt)

#
# from itertools import *
# cnt = 0
# for p in product("ЛЮСТРА", repeat = 5):
#     p = "".join(p)
#     if p.count("Ю") <= 2:
#         if p[-1] not in "ЛСТР":
#             cnt += 1
# print(cnt)
#
# from itertools import *
# cnt = 0
# for p in product("АЛГОРИТМ", repeat = 6):
#     p = "".join(p)
#     if p.count("Л") <= 1:
#         if p[0] != "Р" and p[-1] not in "ЛГРТМ":
#             cnt += 1
# print(cnt)

# from itertools import *
# num = 0
# for p in product("01234567", repeat = 5):
#     p = "".join(p)
#     if p[0] != '0':
#         copied3 = [x for x in p if p.count(x) == 3]
#         copied1 = [x for x in p if p.count(x) == 1]
#         if len(copied3) == 3 and len(copied1) == 2:
#             if copied3[0] * 3 in p:
#                 num += 1
# print(num)

# from itertools import *
# cnt = 0
# for p in set(permutations("СОТОЧКА", r= 7)):
#     p = "".join(p)
#     if "ОА" in p or "АО" in p:
#         cnt += 1
# print(cnt)

# from itertools import *
# n = []
# for p in permutations('СОТОЧКА'):
#     word = ''.join(p)
#     if 'ОО' in word or 'ОА' in word or 'АО' in word:
#         n.append(word)
#         print(word)
# print(len(set(n)))


# from itertools import product
# n = 0
# l = []
# for p in product(sorted("МАРКСЛ"), repeat = 6):
#     p = "".join(p)
#     n += 1
#     # chis1 = [x for x in p if p.count(x) == 3] как бы разбиваем строчку
#     chis1 = [x for x in p if p.count(x) == 3]
#     # chis2 = [x for x in p if p.count(x) == 1] здесь то же самое
#     chis2 = [x for x in p if p.count(x) == 1]
#     # if len(chis1) == 3 and len(chis2) == 3: проверяес длину как бы разбитой строки
#     if len(chis1) == 3 and len(chis2) == 3:
#         if "КС" not in p and "СК" not in p:
#             l.append(n)
# print(max(l))

# from itertools import product
# cnt = 0
# for p in product("0123456789ABCDE", repeat = 5):
#     p = "".join(p)
#     if p[0] != "0":
#         bol = [x for x in p if x > "9"]
#         if len(bol) >= 2:
#             if p.count("8") == 1:
#                 cnt += 1
# print(cnt)

# from itertools import product
# k = 0
# # for x in product(sorted('0123456789"AAAAA"'), repeat=5): гениально ААААА
#     s = ''.join(x)
#     if s[0]!='0' and s.count('8')==1 and s.count('A')>=2:
#         k+=1
# print(k)
#
# from itertools import product
# n = 0
# l = []
# for p in product(sorted("ПЯТЬДНЕЙ"), repeat = 4):
#     p = "".join(p)
#     n += 1
#     if len(p) == len(set(p)):
#         for x in "ЯЕ":
#             p = p.replace(x, "*")
#         if p.count("*") == 0:
#             l.append(n)
# print(max(l))

# from itertools import product
# cnt = 0
# for p in product("ВЬЮГА", repeat = 6):
#     p = "".join(p)
#     if "ЮГ" in p:
#         print(p)
#         cnt += 1
# print(cnt)

# from itertools import *
# n = 0
# for  p in product(sorted("ПОБЕДА"), repeat = 6):
#     p = "".join(p)
#     n += 1
#     if n % 2 == 0:
#         if p[0] == "О":
#             if len(p) == len(set(p)):
#                 print(n)

# from itertools import *
# n = 0
# for p in product("ЖИВОДЁРНЯ", repeat = 5):
#     p = "".join(p)
#     n += 1
#     if n % 2 == 0:
#         if p[0] == p[-1]:
#             if p.count("Р") >= 2:
#                 print(p, n)

# from itertools import *
# n  = 0
# for p in product("БУРАТИНО", repeat = 5):
#     p = "".join(p)
#     n += 1
#     if n % 2 != 0:
#         if p[0] not in "УАИО":
#             if len(p) == len(set(p)):
#                 print(n, p)

# from itertools import *
# n = 0
# for p in product("КОМПЬЮТЕР", repeat= 5):
#     p = "".join(p)
#     n += 1
#     if n % 2 != 0:
#         if p[0] not in "КО":
#             if p.count("Т") >= 3:
#                 print(n, p)

# from itertools import *
# n = 0
# l = []
# for p in product(sorted("ФОКУС"), repeat = 5):
#     p = "".join(p)
#     n += 1
#     if p.count("Ф") == 0:
#         if p.count("У") == 2:
#             l.append(n)
# print(max(l))

# from itertools import *
# n = 0
# for p in product(sorted("ФЕВРАЛЬ"), repeat = 6):
#     p = "".join(p)
#     n += 1
#     if "Е" not in p and "А" not in p:
#         print(n)
#         break

# from itertools import permutations
# cnt = 0
# for p in set(permutations("КЛАБХАУС")):
#     p = "".join(p)
#     if "АА" not in p:
#         cnt += 1
#         print(cnt)  ***

# from itertools import *
# cnt = 0
# for p in product("01234567", repeat = 5):
#     if p[0] != "0":
#         p = "".join(p)
#         # if p[0] not in "1357":
#         if int(p[0]) % 2 == 0:
#             # if p[-1] not in "26": 9135
#             if p[-1] != "2" and p[-1] != "6":
#                 if p.count("7") <= 2:
#                     cnt += 1
# print(cnt)



# from itertools import *
# cnt = 0
# for p in product("01234567", repeat = 7):
#     if p[0] != "0":
#         p = "".join(p)
#         if p.count("0") == 2:
#             for x in "1357":
#                 p = p.replace(x, "*")
#             for x in "0246":
#                 p = p.replace(x, "-")
#             if "**" not in p or "--" not in p:
#                 cnt += 1
# print(cnt)

# from itertools import *
# cnt = 0
# for p in product("ЯНВАРЬ", repeat = 5):
#     p = "".join(p)
#     cnt += 1
#     if p[0] != "Я":
#         if p.count("Ь") <= 1:
#             if "ЯЯ" not in p:
#                 print(cnt, p)

# from itertools import *
# n = 0
# for p in product(sorted("ВЕНЕРА"), repeat = 5):
#     p = "".join(p)
#     n += 1
#     if p[0] != "Н":
#         if p.count("В") == 2:
#             print(n)

# from itertools import *
# n = 0
# for p in product(sorted("ФОКУС"), repeat = 5):
#     p = "".join(p)
#     if p.count("Ф") == 0 and p.count("У") == 2:
#         print(n)
#     n += 1

# from itertools import *
# cnt = 0
# for p in product(sorted("АЛГОРИТМ"), repeat = 5):
#     p = "".join(p)
#     cnt += 1
#     if cnt % 2 == 0:
#         if p[0] not in "ТР":
#             if p.count("И")>=2:
#                 print(cnt)

# from itertools import *
# cnt = 0
# for p in product("0123456", repeat= 5):
#     if p[0] != "0":
#         p = "".join(p)
#         if p.count("6") == 1:
#             for i in p:
#                 if p.count(i) > 1:
#                     p = p.replace(i, "*")
#             if "**" not in p:
#                 cnt += 1
# print(cnt)



# def summ(x):
#     l = []
#     for i in x:
#         l.append(int(i))
#     return sum(l)
#
# n = 0
# for pech in range(0, 23+1):
#     for vtorch in range(0, 59+1):
#         if pech % 2 == 0 and vtorch % 2 == 0:
#             if summ(str(pech)) == summ(str(vtorch)):
#                 n += 1
# print(n)
