# region 📚 Шпаргалка ЕГЭ | Задание №9

# Задание №1:
# Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
#
# – квадрат наибольшего значения больше произведения остальных чисел;
# – сумма двух наибольших значений как минимум вдвое больше суммы остальных значений в строке.

# Решение:
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if (max(M) ** 2) > (M[0]*M[1]*M[2]*M[3]*M[4]) / max(M):
        if (M[-1]+M[-2]) / (M[0]+M[1]+M[2]) >= 2:
            count += 1
print(count)
'''

# Задание №2:
# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнено хотя бы одно из условий:
#
# – в строке есть хотя бы одно повторяющееся число;
# – будучи упорядоченными, все числа строки образуют арифметическую прогрессию.

# Решение:
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(i) for i in s.split()])
    if len(set(M)) != len(M) or all(M[i + 1] - M[i] == M[1] - M[0] for i in range(len(M) - 1)):
        count += 1
print(count)
'''

# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 9 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1472
# 💡 Работа с файлами Python: https://t.me/informatika_kege_itpy/286
# 🐍 Примеры работы с .txt файлами на некоторых номерах ЕГЭ: https://t.me/informatika_kege_itpy/400
# endregion (не удаляйте меня, я тут не просто так)


# cnt = 0
# for s in open("files/dz 1.csv"):
#     m = sorted([int(i) for i in s.split(",")])
#     total = 1
#     for i in m[:4]:
#         total *= i
#     if max(m)**2 > total:
#         if max(m) + m[-2] >= (sum(m) - max(m) - m[-2])*2:
#             cnt += 1
# print(cnt)

# from math import prod
# cnt = 0
# for s in open("files/dz 2.csv"):
#     m = [int(i) for i in s.split(",")]
#     if sum(m) % 18 == 0 or prod(m) == 18**5:
#         cnt += 1
# print(cnt)


# cnt = 0
# for s in open("files/dz 5.csv"):
#     m = sorted([int(i) for i in s.split(",")])
#     if (min(m) + max(m))*3 <= (m[1]+m[2]+m[3])*2:
#         print(m)
#         k = 0
#         for i in m:
#             if m.count(i) == 1:
#                 k += 1
#             if k == 5:
#                 cnt += 1
# print(cnt)

# cnt = 0
# for s in open("files/dz 6.csv"):
#     m = sorted([int(i) for i in s.split(",")])
#     k = 0
#     p = 0
#     for i in m:
#         if i % 3 == 0:
#             k += 1
#             p += i
#     if k == 3:
#         if max(m)-min(m) <= p:
#             cnt += 1
# print(cnt)

# from math import prod
# cnt = 0
# for s in open("files/dz 9.csv"):
#     m = sorted([int(i) for i in s.split(",")])
#     if len(m) == len(set(m)):
#         if (max(m)+min(m))**2 > prod(m[1:3]):
#             cnt += 1
# print(cnt)

# from math import floor
# cnt = 0
# for s in open("files/dz 12.csv"):
#     m = [int(i) for i in s.split(",")]
#     l = floor(sum(m)/len(m))
#     if l in m:
#         cnt += 1
# print(cnt)

# cnt = 0
# for s in open("files/dz 3.csv"):
#     m = [int(i) for i in s.split(",")]
#     a = [x for x in m if x % 2 == 0]
#     k = 0
#     for i in m:
#         if i in a:
#             k += 1
#     if k >= 4:
#         if len(m) == len(set(m)):
#             cnt += 1
# print(cnt)

# cnt = 0
# for s in open("files/9.csv"):
#     m = [int(i) for i in s.split(";")]
#     if len(m) == len(set(m)):
#         m = sorted(m)
#         if m[0] + m[-1] <= sum(m[1:4]):
#             cnt += 1
# print(cnt)
#
# cnt = 0
# for i in open("files/9_22222.csv"):
#     m = [int(p) for p in i.split(";")]
#     if m.count(max(m)) == 1:
#         l = [x for x in m if m.count(x) == 2]
#         l1 = sorted([x for x in m if m.count(x) == 1])
#         if len(l) == 2 and len(l1) == 4:
#             m = sorted(m)
#             for i in range(len(m)-1):
#                 x, y = m[i], m[i+1]
#                 if x == y:
#                     if x * y >= (l1[0]**2 + l1[1]**2):
#                         cnt += 1
# print(cnt)

# cnt = 0
# for i in open("files/9_19241.csv"):
#     m = [int(p) for p in i.split(";")]
#     cnt += 1
#     l = [x for x in m if m.count(x) == 3]
#     l1 = [x for x in m if m.count(x) == 1]
#     if len(l) == 6 and len(l1) == 1:
#         if sum(l) // 6 < int(l1[0]):
#             print(cnt)
#
# cnt = 0
# for i in open("files/9_22222.csv"):
#     m = [int(p) for p in i.split(";")]
#     if m.count(max(m)) == 1:
#         l2 = [x for x in m if m.count(x) == 2]
#         l1 = [x for x in m if m.count(x) == 1]
#         if len(l2) == 2 and len(l1) == 4:
#             m = sorted(l1)[:2]
#             if l2[0] ** 2 <= m[0] ** 2 + m[1] ** 2:
#                 cnt += 1
# print(cnt)


# cnt  =0
# for s in open("files/9_0JcUYgk (1).csv"):
#     m = sorted([int(x) for x in s.split(";")])
#     s = [x for x in m if x % 2 == 0]
#     if len(s) == 4:
#         if m[0]**2 <= sum(m[1:]):
#             cnt += 1
# print(cnt)
# cnt = 0
# for s in open("files/9_17863.csv"):
#     m = [int(i) for i in s.split(";")]
#     l = [x for x in m if m.count(x) == 3]
#     l1 = [x for x in m if m.count(x) == 1]
#     if len(l) == 3 and len(l1) == 3:
#         if sum(l)**2 > sum(l1)**2:
#             cnt += 1
# print(cnt)

# cnt = 0
# for s in open("files/9_23268.csv"):
#     m = [int(i) for i in s.split(";")]
#     cnt += 1
#     l = [x for x in m if m.count(x) == 2]
#     l1 = [x for x in m if m.count(x) == 1]
#     if len(l) == 4 and len(l1) == 3:
#         if sum(l) / 4 < max(l1):
#             print(cnt)
#             break
# cnt = 0
# for s in open("files/9______23440.csv"):
#     m = [int(i) for i in s.split(";")]
#     l = [x for x in m if m.count(x) == 3]
#     l1 = [x for x in m if m.count(x) == 1]
#     if len(l) == 6 and len(l1) == 1:
#         if max(l) > max(l1):
#             cnt += 1
# print(cnt)

# n = 0
# for s in open("files/9_23368.csv"):
#     m = sorted([int(i) for i in s.split(";")])
#     n += 1
#     if len(m) == len(set(m)):
#         l = (max(m) + min(m))*2
#         l1 = sum(m[1:4]) * 3
#         if l == l1:
#             print(n, m, l, l1)

# n = 0
# for s in open("files/9 (1).csv"):
#     m = [int(i) for i in s.split(";")]
#     n += 1
#     m1 = [x for x in m if m.count(x) == 2]
#     m2 = [x for x in m if m.count(x) == 1]
#     if len(m1) == 4 and len(m2) == 2:
#         if min(m) not in m1:
#             if max(m) not in m1:
#                 print(m, n)
#                 break