
# region 📚 Шпаргалка ЕГЭ | Задание №13

# Задание №1:
# По заданным IP-адресу узла и маске определите адрес сети.
#
# IP-адрес узла: 64.128.208.194
# Маска: 255.255.224.0
#
# При записи ответа выберите из приведённых в таблице чисел четыре элемента IP-адреса сети и запишите
# в нужном порядке соответствующие им буквы без использования точек.
#
# A	B	C	D	E	F	G	H
# 0	64	128	192	194	208	224	255

# Решение:
'''
# from ipaddress import *
# net = ip_network('64.128.208.194/255.255.224.0', 0)
# print(net)  # 64.128.192.0/19, где 19 - кол-во единиц в маске числа
'''


# Задание №2:
# Для узла с IP-адресом 111.81.176.27 адрес сети равен 111.81.160.0.
# Чему равен третий слева байт маски?
# Ответ запишите в виде десятичного числа.

# Решение:
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'111.81.176.27/{mask}', 0)
    print(net, net.netmask)
    # 111.81.160.0/19 255.255.224.0
'''


# Задание №3:
# Для узла с IP-адресом 163.232.136.60 адрес сети равен 163.232.136.0.
# Найдите наибольшее возможное количество единиц в двоичной записи маски подсети.

# Решение:
'''
from ipaddress import *
maxi = 0
for mask in range(32+1):
    net = ip_network(f'163.232.136.60/{mask}', 0)
    if str(net) == f'163.232.136.0/{mask}':
        maxi = max(maxi, mask)
print(maxi)
'''


# Задание №4:
# Сеть задана IP-адресом 136.36.240.16 и маской сети 255.255.255.248.
# Сколько в этой сети IP-адресов, в которых в двоичной записи IP-адреса не встречается 101?

# Решение:
'''
from ipaddress import *
net = ip_network('136.36.240.16/255.255.255.248', 0)
cnt = 0
for ip in net:
    if '101' in f'{ip:b}':
        cnt += 1
print(cnt)
'''


# Задание №5:
# Сеть, в которой содержится узел с IP-адресом 223.167.A.167, задана маской сети 255.255.255.192,
# где A - некоторое допустимое для записи IP-адреса число.
# Определите максимальное значение A,
# для которого для всех IP-адресов этой сети в двоичной записи IP-адреса суммарное количество нулей
# в левых двух байтах не больше суммарного количества нулей в правых двух байтах.
#
# В ответе укажите только число.

# Решение:
'''
from ipaddress import *
maxi = 0
for A in range(0, 255+1):
    net = ip_network(f'223.167.{A}.167/255.255.255.192', 0)
    if all(f'{ip:b}'[:16].count('0') <= f'{ip:b}'[16:].count('0') for ip in net):
        maxi = A
print(maxi)
'''


# Задание №6:
# Узлы с IP-адресами 120.91.176.213 и 120.91.174.205 находятся в одной сети.
# Укажите наибольшее возможное значение третьего слева байта маски этой сети.
# Ответ запишите в виде десятичного числа.

# Решение:
'''
from ipaddress import *
for mask in range(32+1):
    net1 = ip_network(f'120.91.176.213/{mask}', 0)
    net2 = ip_network(f'120.91.174.205/{mask}', 0)
    if net1 == net2:
        print(net1.netmask)
'''


# Задание №7:
# Два узла, находящиеся в одной сети, имеют IP-адреса 121.171.5.70 и 121.171.5.107.
# Укажите наименьшее возможное количество адресов в этой сети.

# Решение:
'''
from ipaddress import *
R = []
for mask in range(32+1):
    net1 = ip_network(f'121.171.5.70/{mask}', 0)
    net2 = ip_network(f'121.171.5.107/{mask}', 0)
    if net1 == net2:
        R.append(net1.num_addresses)
print(min(R))
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 13 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1533
#  🐍 Библиотека ipaddress в Python: https://t.me/informatika_kege_itpy/397
# endregion (не удаляйте меня, я тут не просто так)


# # todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
# progress_result = ()  # Сюда заносятся номера, прорешанных задач.
# print('Рекомендуемое кол-во решенных задач для закрепления номера 30.')
# print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 30))}% задач прорешано.')


# from ipaddress import *
# ap = ip_network("191.128.66.83/255.192.0.0", False)
# print(ap[-2])

# from ipaddress import *
# ap = ip_network("102.162.200.51/255.255.255.0", False)
# print(ap[-2])
# a = 102+162+200+254
# print(a)

# from ipaddress import *
# cnt = 0
# ap = ip_network("172.16.80.0/0.0.7.255", False)
# for i in ap:
#     i = bin(int(i))[2:]
#     if i.count("1") % 3 != 0:
#         cnt += 1
# print(cnt)

# from ipaddress import *
# ap = ip_network("143.168.72.213/255.255.255.240", False)
# print(ap[-2])

# from ipaddress import *
# cnt = 0
# ap = ip_network("203.68.128.0/255.255.192.0", False)
# for i in ap:
#     i = bin(int(i))[2:]
#     if i.count("1") % 7 != 0:
#         cnt += 1
# print(cnt)

# from ipaddress import *
# ap = ip_network("158.214.121.40/255.255.255.224", False)
# for i in ap:
#     print(i)


# from ipaddress import *
# net = ip_network("205.99.68.249/255.255.248.0", False)
# for i in net:
#     print(i)


# from ipaddress import *
# net = ip_network("172.140.68.0/255.255.248.0", False)
# cnt = 0
# for i in net:
#     i = bin(int(i))[2:].zfill(32)
#     if i.count("0") > 15:
#         cnt += 1
# print(cnt)

# from ipaddress import *
# for masc in range(16, 32):
#     cnt = 0
#     net = ip_network(f"143.131.211.37/{masc}", False)
#     for i in net:
#         i = bin(int(i))[2:].zfill(32)
#         if i.count("1") == 10:
#             cnt += 1
#     if cnt == 15:
#         print(masc)


# from ipaddress import *
# cnt = 0
# net = ip_network("5.2.5.0/255.255.0.0", False)
# for i in net:
#     i = bin(int(i))[2:].zfill(32)
#     if i.count("0") % 25 == 0:
#         cnt += 1
# print(cnt)

# from ipaddress import *
# cnt = 0
# net = ip_network("192.168.248.176/255.255.255.240", False)
# for i in net:
#     i = bin(int(i))[2:].zfill(32)
#     if i.count("1") == i.count("0"):
#         cnt += 1
# print(cnt)

# from ipaddress import *
# cnt = 0
# net = ip_network("192.168.248.176/255.255.255.240")
# for i in net:
#     i = bin(int(i))[2:].zfill(32)
#     if i.count("0") == i.count("1"):
#         cnt += 1
# print(cnt)

# from ipaddress import *
# net = ip_network("11.92.135.56/255.224.0.0", False)
# print(net[-2])

# from ipaddress import *
# cnt = 0
# net = ip_network("172.16.192.0/255.255.192.0", False)
# for i in net:
#     l = bin(int(i))[2:].zfill(32)
#     if int(i) % 2 != 0:
#         if l.count("1") % 3 == 0:
#             cnt += 1
# print(cnt)

# from ipaddress import *
# net = ip_network("150.122.11.21/255.255.254.0", False)
# n = bin(int(net[1]))[2:].zfill(32)
# print(n.count("1"))

# from ipaddress import *
# net = ip_network("172.96.132.47/255.240.0.0", False)
# print(int(net[-2]))

# from ipaddress import *
# net = ip_network("142.36.195.251/255.255.255.192", False)
# print((net[1]))
# from ipaddress import *
# net = ip_network("218.194.82.148/255.255.255.192", False)
# print(net[-2])

# from ipaddress import *
# net = ip_network("192.168.32.64/255.255.255.192", False)
# cnt = 0
# for i in net:
#     s = f"{i:b}"
#     if s[-3:] == "101":
#         cnt += 1
# print(cnt)

# from ipaddress import *
# net = ip_network("192.168.32.128/255.255.255.192", False)
# cnt = 0
# for i in net:
#     s = f"{i:b}"
#     if s.count("1") % 2 == 0:
#         cnt += 1
# print(cnt)

# from ipaddress import *
# net = ip_network("203.111.195.0/255.255.240.0", False)
# cnt = 0
# for i in net:
#     s = f"{i:b}"
#     if s.count("0") % 3 == 0:
#         if "111" in s:
#             if "000" in s:
#                 cnt += 1
# print(cnt)

# from ipaddress import *
# for masc in range(32+1):
#     net1 = ip_network(f"216.54.187.235/{masc}", 0)
#     net2 = ip_network(f"216.54.174.128/{masc}", 0)
#     if net1 != net2:
#         print(net1.netmask)
#         print(masc)
"""
from ipaddress import *
for masc in range(32+1):
    net1 = ip_network(f"157.127.172.56/{masc}", 0)
    net2 = ip_network(f"157.127.191.78/{masc}", 0)
    if net1 != net2:
        print(masc)
"""

# from ipaddress import *
# cnt = 0
# net = ip_network("213.232.128.145/255.255.128.0", False)
# for i in net:
#     s = f"{i:b}"
#     if s.count("0") % 5 == 0:
#         cnt += 1
# print(cnt)


# from ipaddress import *
# cnt = 0
# net = ip_network("172.16.192.0/255.255.192.0", False)
# for i in net:
#     s = f"{i:b}"
#     if s.count("1") % 5 != 0:
#         cnt += 1
# print(cnt)

# from ipaddress import *
# net = ip_network("140.37.235.224/255.255.240.0", 0)
# print(net[0])

# from ipaddress import *
# l = []
# for x in range(32+1):
#     net = ip_network(f"163.232.136.0/{x}", 0)
#     net1 = ip_network(f"163.232.136.60/{x}", 0)
#     if net1 == net:
#         l.append(x)
# print(max(l))
#
# from ipaddress import *
# cnt = 0
# net = ip_network("136.36.240.16/255.255.255.248", False)
# for i in net:
#     s = f"{i:b}"
#     if "101" not in s:
#         cnt += 1
# print(cnt)

# from ipaddress import *
# l = []
# for masc in range(32+1):
#     net1 = ip_network(f"165.112.200.70/{masc}", 0)
#     net2 = ip_network(f"165.112.175.80/{masc}", 0)
#     if net1 == net2:
#         l.append(masc)
# print(max(l))

# from ipaddress import *
# net = ip_network("217.19.128.131/255.255.192.0", False)
# print(net[0])

#from ipaddress import *
# # for masc in range(32+1):
# #     net1 = ip_network(f"111.91.192.0/{masc}", 0)
# #     if ip_address("111.91.200.28") in net1:
# #         print(f"{net1.netmask:b}")
# # print(a.count("0"))


# from ipaddress import *
# cnt = 0
# net = ip_network("192.168.32.48/255.255.255.240", False)
# for i in net:
#     s = f"{i:b}"
#     if s.count("1") % 2 != 0:
#         cnt +=1
# print(cnt)

# from ipaddress import *
# for masc in range(32+1):
#     net1 = ip_network(f"10.96.180.231/{masc}", 0)
#     net2 = ip_network(f"10.96.140.118/{masc}", 0)
#     if net1 != net2:
#         l = (f"{net1.netmask:b}")
#         print(l.count("0"))
#         break

# from ipaddress import *
# net = ip_network("10.8.248.131/255.255.224.0", False)
# print(net[0])

# from ipaddress import *
# l =[]
# for masc in range(32+1):
#     net1 = "133.57.64.0"
#     net2 = ip_network(f"133.57.64.130/{masc}", False) ****
#     if net1 in str(net2):*******
#         l.append(masc) ******
# print(len(l))

# from ipaddress import *
# cnt = 0
# net = ip_network("192.168.32.160/255.255.255.240", False)
# for i in net:
#     s = f"{i:b}"
#     if s.count("0") > 21:
#         cnt += 1
# print(cnt)

# from ipaddress import *
# net = ip_network("185.8.0.0/255.255.128.0", False)
# s = net[-1]
# s1 = f"{s:b}"
# print(s1.count("1"))

# from ipaddress import *
# net = ip_network("158.214.121.40/255.255.255.224", False)
# print(net[-2])

# from ipaddress import *
# for masc in range(0, 32+1):
#     net = ip_network(f"73.148.145.65/{masc}", False)
#     if net.netmask:
#         print(net, net.netmask)
#
# net = ip_network("73.128.0.0/255.224.0.0", False)
# print(net[-2])



from ipaddress import *
for masc in range(32+1):
    net = ip_network(f"202.54.79.201/{masc}", False)
    if net.netmask:
        print(net, net.netmask)

net = ip_network("202.54.78.0/255.255.254.0", False)
print(net[-2])