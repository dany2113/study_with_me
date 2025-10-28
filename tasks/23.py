
# region 📚 Шпаргалка ЕГЭ | Задание №23

# Задание №1:
# Исполнитель преобразует число на экране. У исполнителя есть три команды, которые обозначены латинскими буквами:
# A. Прибавить 1
# B. Умножить на 2
# C. Возвести в квадрат
# Сколько существует программ, для которых при исходном числе 2 результатом является число 40,
# при этом траектория вычислений содержит число 10, не содержит числа 11 и не содержит числа 12?

# Решение:
'''
def F(a, b):
    if (a > b) or (a == 11) or (a == 12):
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a * 2, b) + F(a ** 2, b)

print(F(2, 10) * F(10, 40))
'''


# Задание №2:
# Исполнитель преобразует число на экране. У исполнителя есть три команды, которые обозначены латинскими буквами:
# A. Найти целую часть от деления на 2
# B. Найти целую часть от деления на 3
# C. Вычесть 3
# Сколько существует программ, для которых при исходном числе 163 результатом является число 3,
# при этом траектория вычислений содержит число 45 и не содержит чисел 36 и 100?

# Решение:
'''
def F(a, b):
    if (a < b) or (a == 36) or (a == 100):
        return 0
    elif a == b:
        return 1
    else:
        return F(a // 2, b) + F(a // 3, b) + F(a - 3, b)

print(F(163, 45) * F(45, 3))
'''


# Задание №3:
# (М. Ишимов) Исполнитель преобразует число на экране.
# У исполнителя есть три команды, которые обозначены латинскими буквами:
# A. Прибавить 2
# B. Возвести в квадрат
# C. Умножить на 3
# Сколько существует программ, для которых при исходном числе 2 результатом является число 64,
# если после выполнения команды B можно выполнить только команду A или C?

# Решение:
'''
def F(a, b, flag):
    if a >= b:
        return a == b
    if flag == "B":
        return F(a + 2, b, "A") + F(a * 3, b, "C")
    return F(a+2, b, "A") + F(a**2, b, "B") + F(a*3, b, "C")

print(F(2, 64, 0))
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 23 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1826
# endregion (не удаляйте меня, я тут не просто так)


# # todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
# progress_result = ()  # Сюда заносятся номера, прорешанных задач.
# print('Рекомендуемое кол-во решенных задач для закрепления номера 30.')
# print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 30))}% задач прорешано.')


# def f(curr, end):
#     if curr>end: return 0
#     if curr==end: return 1
#     if curr<end: return f(curr+1, end) + f(curr+3, end) + f(curr*2, end)
# print(f(3, 10)*f(10, 20)*f(20, 30))

# def f(c, e):
#     if c < e: return 0
#     if c == e: return 1
#     if c > e: return f(c - 1, e) + f(c - 3, e) + f(c // 3, e)
# print(f(22, 2))

# def f(c, e):
#     if c > e or c == 21: return 0
#     if c == e: return 1
#     if c < e: return f(c+1, e) + f(c*2+1, e)
# print(f(1, 25))

# def f(c, e):
#     if c < e: return 0
#     if c == e: return 1
#     if c > e: return f(c - 8, e) + f(c // 2, e)
# print(f(102, 43) * f(43, 5))

# def f(c, e):
#     if c > e or c == 10: return 0
#     if c == e: return 1
#     if c < e: return f(c + 1, e) + f(c + 2, e) + f(c * 3, e)
# l = f(1, 7) * f(7, 25)



# print(l)
# def f(c, e):
#     if c > e or c == 7: return 0
#     if c == e: return 1
#     if c < e: return f(c + 1, e) + f(c + 2, e) + f(c * 3, e)
# l1 = f(1, 10) * f(10, 25)
# print(l1)
#
# print(l + l1)


# def f(c, e):
#     if c > e or c == 16: return 0
#     if c == e: return 1
#     if c < e:
#         return f(c+1, e) + f(c*3, e) + f(c + 5, e)
# print(f(2, 7) * f(7, 21))


# def f(c, e):
#     if c > e: return 0
#     if c == e: return 1
#     if c < e: return f(c+1, e) + f(c * 3, e)
# print(f(2, 56))

# def f(c, e):
#     if c > e: return 0
#     if c == e: return 1
#     if c < e: return f(c + 1, e) + f(c * 3, e) + f(c ** 2, e)
# print(f(4, 93))

# def f(c, e):
#     if c > e or c == 27: return 0
#     if c == e: return 1
#     if c < e: return f(c+2, e) + f(c*2, e)
# print(f(3, 15)*f(15, 72))

# def f(c, e):
#     if c > e or c == 44: return 0
#     if c == e: return 1
#     if c < e: return f(c+2, e) + f(c*3, e)
# print(f(2, 24)*f(24, 144))

# def f(c, e):
#     if c < e: return 0
#     if c == e: return 1
#     if c > e: return f(c-1, e) + f(c//3, e)
# print(f(49, 11)*f(11, 1))

# def f(c, e):
#     if c > e: return 0
#     if c == e: return 1
#     if c < e: return f(c+1, e) + f(c+10, e) 2 - ой - при условии увеличеснии числа десятков на 1 (прибавляем десять)
# print(f(2, 45))

# def f(c, e):
#     if c > e: return 0
#     if c == e: return 1
#     if c < e: return f(c+2, e) + f(c*2, e) + f((c*2)+1, e)
# print(f(3, 90))

# def f(c, e):
#     if c > e: return 0
#     if c == e: return 1
#     if c < e: return f(c+1, e) + f(int(str(c)+"1"), e)
# print(f(1, 928))

# def f(c, e):
#     if c > e: return 0
#     if c == e: return 1
#     if c < e: return f(c+1, e) + f(c * 2, e)
# print(f(1, 16))

# def f(c, e):
#     if c > e: return 0
#     if c == e: return 1
#     if c < e: return f(c+2, e) + f(c*2, e) + f(c*2 +1 , e)
# print(f(1, 24))

# def f(c, e):
#     if c > e: return 0
#     if c == e: return 1
#     if c < e: return f(c+1, e) + f(c+10, e)
# print(f(12, 27))

# def f(c, e):
# #     if c < e: return 0
# #     if c == e: return 1
# #     if c > e: return f(c-1, e) + f(c // 3, e)
# # print(f(33, 7) * f(7, 2))

# def f(c, e):
#     if c > e or c == 19: return 0
#     if c == e: return 1
#     if c < e: return f(c+1, e) + f(c * 2, e)
# print(f(2, 29))

# def f(c, e):
#     if c > e or c == 30: return 0
#     if c == e: return 1
#     if c < e: return f(c+1, e) + f(c*3, e)
# print(f(3, 20)*f(20, 80))

# def f(c, e):
#     if c > e: return 0
#     if c == e: return 1
#     if c < e: return f(c+2, e) + f(c*3, e) + f(c**2, e)
# print(f(3, 77))

# def f(c, e):
#     if c > e: return 0
#     if c == e: return 1
#     if c < e: return f(c+1, e) + f(c*3, e)
# print(f(2, 52))

# def f(c, e):
#     if c > e or c == 10: return 0
#     if c == e: return 1
#     if c < e: return f(c+1, e) + f(c+2, e) + f(c*3, e)
# l1 = (f(1, 7) * f(7, 25))
# def f(c, e):
#     if c > e or c == 7: return 0
#     if c == e: return 1
#     if c < e: return f(c+1, e) + f(c+2, e) + f(c*3, e)
# l = (f(1, 10) * f(10, 25))
#
# print(l + l1)

# def f(c, e):
#     if c > e or c == 10: return 0
#     if c == e: return 1
#     if c < e: return f(c+1, e) + f(c+2, e) + f(c*2, e)
# print(f(3, 7) * f(7, 20))

def f(c, e):
    if c > e or c % 3 == 0: return 0
    if c == e: return 1
    if c < e: return f(c-1, e) + f(c+3, e) + f(c*2, e)
print(f(5, 100))