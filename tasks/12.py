
# region 📚 Шпаргалка ЕГЭ | Задание №12

# Задание №1:
# Дана программа для Редактора:
#
# НАЧАЛО
#    ПОКА нашлось (11)
#       заменить (112, 4)
#       заменить (113, 2)
#       заменить (42, 3)
#       заменить (43, 1)
#    КОНЕЦ ПОКА
# КОНЕЦ
# Какая строка получится в результате применения приведённой программы к строке
# вида 1…13…32…2 (170 единиц, 100 троек и 7 двоек)?

# Решение:
'''
s = 170 * '1' + 100 * '3' + 7 * '2'

while '11' in s:
    s = s.replace('112', '4', 1)
    s = s.replace('113', '2', 1)
    s = s.replace('42', '3', 1)
    s = s.replace('43', '1', 1)

print(s)
'''


# Задание №2:
# Дана программа для Редактора:
#
# НАЧАЛО
#    ПОКА нашлось (333) ИЛИ нашлось (555)
#       ЕСЛИ нашлось (555)
#          ТО заменить (555, 3)
#          ИНАЧЕ заменить (333, 5)
#       КОНЕЦ ЕСЛИ
#    КОНЕЦ ПОКА
# КОНЕЦ
# На вход приведённой выше программе поступает строка, начинающаяся с цифры «3»,
# а затем содержащая n цифр «5» (3 <n< 10000).
#
# Определите наибольшее возможное значение суммы числовых значений цифр в строке,
# которая может быть результатом выполнения программы.

# Решение:
'''
M = []
for n in range(3, 10000):
    s = '3' + '5' * n
    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '3', 1)
        else:
            s = s.replace('333', '5', 1)

    sum_digits = [int(i) for i in s]
    M.append(sum(sum_digits))

print(max(M))
'''


# Задание №3:
# Дана программа для Редактора:
#
# НАЧАЛО
# ПОКА нашлось (52) ИЛИ нашлось (2222) ИЛИ нашлось (1122)
#    ЕСЛИ нашлось (52)
#      ТО заменить (52, 11)
#    КОНЕЦ ЕСЛИ
#    ЕСЛИ нашлось (2222)
#      ТО заменить (2222, 5)
#    КОНЕЦ ЕСЛИ
#    ЕСЛИ нашлось (1122)
#      ТО заменить (1122, 25)
#    КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ
# На вход приведённой выше программе поступает строка, начинающаяся с цифры «5»,
# а затем содержащая n цифр «2» (3 < n < 10 000).
#
# Определите наименьшее значение n, при котором сумма цифр в строке,
# получившейся в результате выполнения программы, оканчивается на 7.

# Решение:
'''
for n in range(4, 10000):
    s = '5' + '2' * n
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        elif '2222' in s:
            s = s.replace('2222', '5', 1)
        elif '1122' in s:
            s = s.replace('1122', '25', 1)

    sum_digits = sum([int(i) for i in s])

    if str(sum_digits)[-1] == '7':
        print(n)
        break
'''


# Задание №4:
# Дана программа для Редактора:
#
# НАЧАЛО
#    ПОКА нашлось(>1) ИЛИ нашлось(>2) ИЛИ нашлось(>3)
#       ЕСЛИ нашлось(>1)
#          ТО заменить(>1, 22>3)
#       КОНЕЦ ЕСЛИ
#       ЕСЛИ нашлось(>2)
#          ТО заменить(>2, 2>)
#       КОНЕЦ ЕСЛИ
#       ЕСЛИ нашлось(>3)
#          ТО заменить(>3, 11>2)
#       КОНЕЦ ЕСЛИ
#    КОНЕЦ ПОКА
# КОНЕЦ
#
# На вход приведённой выше программы поступает строка, начинающаяся с символа «>»,
# а затем содержащая n цифр 1, n цифр 2 и n цифр 3 (3 ≤ n ≤ 50),
# расположенных в произвольном порядке.
# Определите количество значений n, при котором сумма числовых значений цифр строки,
# получившейся в результате выполнения программы кратна 7.

# Решение:
'''
count = 0

for n in range(3, 50 + 1):
    s = '>' + '1' * n + '2' * n + '3' * n
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '22>3', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>3' in s:
            s = s.replace('>3', '11>2', 1)

    sum_digits = sum([int(i) for i in s if i.isdigit()])

    if sum_digits % 7 == 0:
        count += 1

print(count)
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 12 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1532
# 💡 Генераторы списков (списочные выражения) для ЕГЭ: https://t.me/informatika_kege_itpy/339
# 🐍 Шпаргалка по генераторам списков: https://t.me/informatika_kege_itpy/495
# 💡 Что такое строки (str) в Python и зачем они нужны: https://t.me/informatika_kege_itpy/265
# endregion (не удаляйте меня, я тут не просто так)


# todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️ 
# progress_result = [1, 2, 3, 21707, 19483] # Сюда заносятся номера, прорешанных задач.
# print('Рекомендуемое кол-во решенных задач для закрепления номера 30.')
# print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 30))}% задач прорешано.')

# d = "5"*30
# while "333" in d or "555" in d:
#     if "333" in d:
#         d = d.replace("333", "5", 1)
#     else:
#         if "555" in d:
#             d = d.replace("555", "3", 1)
# print(d)

# d = "1"*9+"2"*22
# while "111" in d or "222" in d:
#     while "111" in d:
#         d = d.replace("111", "2", 1)
#     while "222" in d:
#         d= d.replace("222", "1", 1)
# print(d)

# d = "5" + "4"*99
# while "54" in d or "644" in d or "7444" in d:
#     if "54" in d:
#         d = d.replace("54", "6", 1)
#     elif "644" in d:
#         d = d.replace("644", "7", 1)
#     else:
#         d = d.replace("7444", "5", 1)
# print(d)

# for n in range(4, 10000):
#     s = "4"+"2"*n
#     while "42" in s or "8222" in s or "2222" in s:
#         if "42" in s:
#             s = s.replace("42", "2", 1)
#         if "8222" in s:
#             s = s.replace("8222", "24", 1)
#         if "2222" in s:
#             s = s.replace("2222", "8", 1)
#     if s.count("8")*8 + s.count("4")*4 + s.count("2")*2 == 110:
#         print(n)
#         break

# for n in range(4, 10000):
#     s = "2"+"5"*n
#     while "25" in s or "355" in s or "555" in s:
#         if "25" in s:
#             s = s.replace("25", "5", 1)
#         if "355" in s:
#             s = s.replace("355", "522", 1)
#         if "555" in s:
#             s = s.replace("555", "3", 1)
#     if s.count("2") == 10:
#         print(n)
#         break

# n = int(input())
# b = [int(i) for i in str(n)]
# b1 = sum(b)
# b2 = 1
# for i1 in b:
#     b2 = i1*b2
# print(b2)
# print(b1)

# n = int(input())
# b = n + int((str(n)) + (str(n))) + int((str(n) + str(n) + str(n)))
# print(b)

# n = "3"*30
# while "333" in n or "555" in n:
#     if "333" in n:
#         n = n.replace("333", "5", 1)
#     else:
#         n = n.replace("555", "3", 1) ans: 55
# print(n)

# s = "1"*9 + "2"*22
# while "111" in s or "222" in s:
#     while "111" in s:
#         s = s.replace("111", "2", 1)
#     while "222" in s:
#         s = s.replace("222", "1", 1) ans: 22112
# print(s)

# s = "5" + "4"*99
# while "54" in s or "644" in s or "7444" in s:
#     if "54" in s:
#         s = s.replace("54", "6", 1)
#     else:
#         if "644" in s:
#             s = s.replace("644", "7", 1)
#         else:
#             s = s.replace("7444", "5", 1) ans: 7
# print(s)

# s = "1"+"4"*81
# while "14"in s or "244" in s or "3444" in s:
#     if "14" in s:
#         s = s.replace("14", "3", 1)
#     if "244" in s:
#         s = s.replace("244", "1", 1)
#     if "3444" in s:
#         s = s.replace("3444", "2", 1) ans: 344
# print(s)

# s = "123" * 456
# while "12" in s or "3333" in s:
#     s = s.replace("12", "3", 1)
#     s = s.replace("3333", "3", 1) ans: 333
# print(s)

# for n in range(91, 300):
#     s = "3"*n
#     while "333" in s:
#         s = s.replace("333", "1", 1)
#         s = s.replace("111", "3", 1)
#     if s == "133":   ans: 93
#         print(n)
#         break

# for n in range(81, 100):
#     s = "2"*n
#     while "222" in s:
#         s = s.replace("222", "5", 1)
#         s = s.replace("555", "2", 1)
#     if s == "5522":  ans: 88
#         print(n)
#         break

# n1 = []
# for n in range(4, 10000):
#     s = "5"+"2"*n
#     while "52" in s or "2222" in s or "3322" in s:
#         if "52" in s:
#             s= s.replace("52", "33", 1)
#         if "2222" in s:
#             s= s.replace("2222", "5", 1)
#         if "3322" in s:
#             s= s.replace("3322", "25", 1)
#     if s.count("3")*3 + s.count("5")*5 + s.count("2")*2 == 83:
#         print(n) ans 65
# n1 = []
# for n in range(4, 10000):
#     s = "3"+"4"*n
#     while "34"in s or "4444" in s or "6644" in s:
#         if "34" in s:
#             s= s.replace("34", "66", 1)
#         if "4444" in s:
#             s = s.replace("4444", "2", 1)
#         if "6644" in s:
#             s = s.replace("6644", "43", 1)
#     if s.count("2")*2 + s.count("4")*4 + s.count("6")*6 == 104:
#         print(n) ans 164

# for n1 in range(1, 100):
#     for n in range(4, 10000):
#         s = "2"+"5"*n
#         while "25"in s or "2222"in s or "2233" in s:
#             if "25" in s:
#                 s = s.replace("25", "33", 1)
#             if "2222" in s:
#                 s= s.replace("2222", "5", 1)
#             if "2233" in s:
#                 s= s.replace("2233", "52", 1)
#         if (s.count("2")*2 + s.count("3")*2 + s.count("5")*5) == n1**2:
#             print(n1, n)
#             break
#
# l = -1
# for n in range(4, 10000):
#     s = "1" + "2"*n
#     while "12" in s or "322" in s or "222" in s:
#         if "12" in s:
#             s = s.replace("12", "2", 1)
#         if "322" in s:
#             s = s.replace("322", "21", 1)
#         if "222" in s:
#             s = s.replace("222", "3", 1)
#     m = s.count("1") + s.count("2") * 2 + s.count("3")*3
#     if m == 17:
#     print(n)

# for n in range(4, 10000):
#     s = "4" + "0" * n
#     while "40" in s or "800" in s or "000" in s:
#         if "40" in s:
#             s = s.replace("40", "0", 1)
#         if "800" in s:
#             s = s.replace("800", "04", 1)
#         if "000" in s:
#             s = s.replace("000", "8", 1)
#     if s.count("4")*4 + s.count("8")*8 == 36:
#         print(n)
#
# for n in range(4, 10000):
#     s = "1" + "2"*n
#     while "12" in s or "322" in s or "222" in s:
#         if "12" in s:
#             s = s.replace("12", "2", 1)
#         if "322" in s:
#             s = s.replace("322", "21", 1)
#         if "222" in s:
#             s = s.replace("222", "3", 1)
#     if s.count("1") + s.count("2")*2 + s.count("3")*3 == 15:
#         print(n)
#         break


# s = "1"*81
# while "111" in s or "88888" in s:
#     if "111" in s:
#         s = s.replace("111", "88", 1)
#     else:
#         s = s.replace("88888", "8", 1)
# print(s)

# for n in range(4, 4000):
#     s = "1" + "2"*n
#     while "12" in s or "312" in s or "222" in s:
#         if "12" in s:
#             s = s.replace("12", "2", 1)
#         if "312" in s:
#             s = s.replace("312", "21", 1)
#         if "222" in s:
#             s = s.replace("222", "311", 1)
#     if s.count("1") == 3:
#         print(n)
# for n in range(4, 10000):
#     s = "1" + "9"*n
#     while "15" in s or "599" in s or "999" in s:
#         if "15" in s:
#             s = s.replace("15", "9", 1)
#         if "599" in s:
#             s = s.replace("599", "5", 1)
#         if "999" in s:
#             s = s.replace("999", "19", 1)
#     if s.count("9")*9 + s.count("5")*5 + s.count("1") == 30:
#         print(n)
#         break