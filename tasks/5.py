
# region 📚 Шпаргалка ЕГЭ | Задание №5

# Задание №1:
# На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
# 1. Строится двоичная запись числа N.
#
# 2. Далее эта запись обрабатывается по следующему правилу:
# а) если сумма цифр в двоичной записи числа чётная, то к этой записи справа дописывается 00,
# а затем два левых разряда заменяются на 11;
# б) если сумма цифр в двоичной записи числа нечётная, то к этой записи справа дописывается 11,
# а затем два левых разряда заменяются на 10.
#
# 3. Пункт 2 повторяется ещё раз к записи, полученной после второго пункта.
# Полученная таким образом запись является двоичной записью искомого числа R.
# Найдите максимальное число R, которое получается при обработке N, меньших 100. В ответе укажите R.

# Решение:
'''
R = []
for n in range(1, 100):
    s = bin(n)[2:]
    for i in range(2):
        if s.count('1') % 2 == 0:
            s = '11' + s[2:] + '00'
        else:
            s = '10' + s[2:] + '11'
    r = int(s, 2)
    R.append(r)
print(max(R))
'''


# Задание №2:
# На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
# 1. Строится троичная запись числа N.
#
# 2. Далее эта запись обрабатывается по следующему правилу:
# а) если сумма цифр троичной записи числа N делится на 4, то слева дописывается «1»,
# а затем из полученной записи удаляются два правых разряда;
# б) если сумма цифр троичной записи числа N на 4 не делится,
# то остаток от деления этой суммы на 4 сначала умножается на 3,
# а затем переводится в троичную запись и дописывается в конец числа.
#
# Полученная таким образом запись является троичной записью искомого числа R.
# 3. Результат переводится в десятичную систему и выводится на экран.
# Укажите минимальное число R, большее 353,
# которое может получиться с помощью описанного алгоритма.

# Решение:
'''
def my_convert(number: int, system: int) -> str:
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    result = ''
    while number > 0:
        result += alphabet[number % system]
        number //= system
    return result[::-1]

R = []
for n in range(1, 10000):
    s = my_convert(n, 3)
    sum_digits = s.count('1') + s.count('2') * 2
    ostat = sum_digits % 4
    if ostat == 0:
        s = '1' + s
        s = s[:-2]
    else:
        ostat = my_convert((ostat * 3), 3)
        s = s + ostat
    r = int(s, 3)
    if r > 353:
        R.append(r)
print(min(R))
'''


# Задание №3:
# На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
# 1. Строится семеричная запись числа N.
#
# 2. Далее эта запись обрабатывается по следующему правилу:
# а) если количество двоек в этой записи чётно, то к ней дописываются 3 пятёрки.
# иначе, если количество двоек в этой записи нечётно, то слева к этой записи дописывается 1 единица.
# Полученная таким образом запись является семеричной записью искомого числа R.
#
# 3. Результат переводится в десятичную систему и выводится на экран.
# Укажите максимальное число N, после обработки которого с помощью этого алгоритма получается число R, меньшее 3799.

# Решение:
'''
def my_convert(number: int, system: int) -> str:
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    result = ''
    while number > 0:
        result += alphabet[number % system]
        number //= system
    return result[::-1]

R = []
for n in range(1, 10000):
    s = my_convert(n, 7)
    if (s.count('2')) % 2 == 0:
        s = s + '555'
    else:
        s = '1' + s
    r = int(s, 7)
    if r < 3799:
        R.append(n)
print(max(R))
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 5 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1465
# 💡 Что такое строки (str) в Python и зачем они нужны: https://t.me/informatika_kege_itpy/265
# 👩‍💻 Все методы списков в Python, которые понадобятся на ЕГЭ: https://t.me/informatika_kege_itpy/344
# 💡 Циклы for и while, как использовать циклы для сдачи КЕГЭ: https://t.me/informatika_kege_itpy/169
# endregion (не удаляйте меня, я тут не просто так)


# # todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
# progress_result = ()  # Сюда заносятся номера, прорешанных задач.
# print('Рекомендуемое кол-во решенных задач для закрепления номера 30.')
# print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 30))}% задач прорешано.')
'''
b = []
for N in range(1, 10000):
    n = bin(N)[2:]
    if N % 2 == 0:
        n = "10" + n
    else:
        n = "1" + n + "01"
    r = int(n, 2)
    if N <= 12:
        print(r)
'''
'''
b = []
for N in range(1, 1000):
    n = bin(N)[2:]
    if N % 3 == 0:
        n = n + n[-3:]
    else:
        n = n + bin((N % 3)*3)[2:]
    r = int(n, 2)
    if r >= 200:
        b.append(N)
print(min(b))
'''

def c6(x):
    s = ""
    while x > 0:
        s = str(x % 6)+s
        x //= 6
    return s

# k = 0
# b = []
# for N in range(1, 10000):
#     n = c6(N)
#     for m in n:
#         k += int(m)
#     if k % 5 == 0:
#         n = n.replace("0", "*").replace("3", "0").replace("*", "3")
#         n = "11" + n
#     else:
#         n += "44"
#         n = n[0] + "05" + n[3:]
#     r = int(n, 6)
#     if r > 1500:
#         print(N)
#         break

# for N in range(1, 10000):
#     n = bin(N)[2:]
#     if len(n) % 2 == 0:
#         n = n + "1"
#     else:
#         n = "1" + n
#     r = int(n, 2)
#     if r > 666:
#         print(N)
# #         break
# l = []
# for N in range(1, 25+1):
#     n = bin(N)[2:]
#     if N % 2 != 0:
#         n = "10" + n + "1"
#     else:
#         n = "10" + n + "0111"
#     re = int(n, 2)
#     l.append(re)
# print(l)
# print(max(l))

# def c3(x):
#     s = ""
#     while x > 0:
#         s = str(x % 3) + s
#         x //= 3
#     return s
#
# for N in range(3, 20000):
#     n = c3(N)
#     if N % 3 == 0:
#         n = n + n[-2] + n[-1]
#     else:
#         n = n + c3(N % 3)
#     r = int(n, 3)
#     if r <= 150:
#         print(N, r)

# def c3(x):
#     s = ""
#     while x > 0:
#         s = str(x % 3) + s
#         x //= 3
#     return s
#
# l = []
# for N in range(1, 10000):
#     n = c3(N)
#     if N % 5 == 0:
#         n = n + n[-2:]
#     else:
#         k = (N % 5) * 2
#         n = n + c3(k)
#     R = int(n, 4)
#     if R <= 514:
#         l.append(R)
# print(max(l))

# def c(x):
#     s = ""
#     while x > 0:
#         s = str(x % 3) + s
#         x //= 3
#     return s
# l = []
# for N in range(1, 10000):
#     n = c(N)
#     if N % 5 == 0:
#         n = n + n[-2:]
#     if N % 5 != 0:
#         n = n + c((N % 5) * 7)
#     r = int(n, 3)
#     if r <= 273:
#         print(N, r)

# def c(x):
#     s = ""
#     while x > 0:
#         s = str(x % 3) + s
#         x //= 3
#     return s
#
# for N in range(1, 10000):
#     n = c(N)
#     if N % 3 == 0:
#         n = n + "10"
#     else:
#         n = n + c((N % 3) * 5)
#     r = int(n, 3)
#     if r > 130:
#         print(N)
#         break

# l = []
# for N in range(1, 10000):
#     n = bin(N)[2:]
#     if n.count("1") % 2 == 0:
#         n = "10" + n + "0"
#     else:
#         n = "1" + n + "11"
#     r = int(n, 2)
#     if r <= 410:
#         l.append(r)
# print(max(l))


# def c3(x):
#     s = ""
#     while x > 0:
#         s = str(x % 3) + s
#         x //= 3
#     return s
#
# l = []
# l1 = []
# for N in range(1, 10000):
#     n = c3(N)
#     if N % 3 == 0:
#         n = n + n[-2:]
#     else:
#         for x in n:
#             l1.append(int(x))
#         n = n + c3(sum(l1))
#     r = int(n, 3)
#     if r > 220:
#         l.append(r)
# print(min(l))

# def c3(x):
#     s = ""
#     while x > 0:
#         s = str(x % 3) + s
#         x //= 3
#     return s
#
# for N in range(1, 1000):
#     n = c3(N)
#     if N % 3 == 0:
#         n = n + n[-3:]
#     else:
#         l = (N % 3) * 3
#         n = c3(l)
#     r = int(n, 3)
#     if r > 344:
#         print(N)
#         break
# l = []
# for N in range(1, 10000):
#     n = bin(N)[2:]
#     if N % 2 == 0:
#         n = "10" + n
#     else:
#         n = "1" + n + "01"
#     r = int(n, 2)
#     if N <= 12:
#         l.append(r)
# print(max(l))

# def c3(x):
#     s = ""
#     while x > 0:
#         s = str(x % 3) + s
#         x //= 3
#     return s
# l = []
# for N in range(1, 10000):
#     n = c3(N)
#     if N % 3 == 0:
#         n = "1" + n + "02"
#     else:
#         n = n + c3((N % 3) * 4)
#     r = int(n, 3)
#     if r < 199:
#         l.append(N)
# print(max(l))


# def c3(x):
#     s = ""
#     while x > 0:
#         s = str(x % 3) + s
#         x //= 3
#     return s
#
# for N in range(1, 10000):
#     n = c3(N)
#     if N % 3 == 0:
#         n = "1" + n + "02"
#     else:
#         n = n + c3((N % 3) * 4)
#     r = int(n, 3)
#     if r < 100:
#         print(N, r)


# def c(x):
#     s = ""
#     while x > 0:
#         s = str( x % 3) + s
#         x //= 3
#     return s
#
# for N in range(1, 10000):
#     n = c(N)
#     l = n.count("1") + n.count("2")*2 + n.count("3")*3
#     if l % 9 == 0:
#         n = n + "2"
#     else:
#         n = n + c(l % 9)
#     r = int(n, 3)
#     if N > 166:
#         print(r, N)
