#--------------------------------------------------
# Programm by Yoatn
#
# Start date   24.10.2017   21:00
# End date     27.10.2017   03:24
#  
# Description:
#Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число n — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.
#
# Sample Input:
# 3
# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2
# Sample Output:
# Зенит:2 2 0 0 6
# ЦСКА:2 0 1 1 1
# Спартак:2 0 1 1 1
#--------------------------------------------------

n = int(input())

g = [[j for j in input().split(';')] for k in range(n)] # # Общий список (матрица)
# print(g)

h = []# Общий список (всё в одной строке)
for i in range(len(g)):
    for j in range(len(g[i])):
        h.append(g[i][j])
# print(h)# Общий список

b = [] # Список только команд (не уникальный)
for x in range(0, len(h), 2):
    b.append(h[x])
c = list(set(b))# Список только команд (уникальный)
# print(c)

# gl = [[0]*5 for x in range(len(c))] # Итоговый список с результатами, матрица (Output)
# for i in range(len(c)):
#     gl[i][0] = c[i]
# print(gl)

d = {}
for i in range(len(c)):
    d[c[i]] = [0, 0, 0, 0, 0]
# print(d)
v = []
for i in range(len(g)):
    for j in range(len(g[i])):
        if int(g[i][1]) > int(g[i][3]):# Победа левого
            v1 = d.get(g[i][0])# Победа левого
            v1[1] += 1
            v1[4] += 3
            v2 = d.get(g[i][2])#Поражение правого
            v2[3] += 1
            break
        if int(g[i][1]) < int(g[i][3]):# Победа правого
            v3 = d.get(g[i][2])# Победа правого
            v3[1] += 1
            v3[4] += 3
            v4 = d.get(g[i][0])#Поражение левого
            v4[3] += 1
            break
        if int(g[i][1]) == int(g[i][3]):#Ничья
            v5 = d.get(g[i][0])
            v5[2] += 1
            v5[4] +=1
            v6 = d.get(g[i][2])
            v6[2] += 1
            v6[4] += 1
            break

for i in range(0, len(h), 2):
    if h[0] in h:
        v7 = d[h[i]]
        v7[0] += 1

# print(d)
m = list(d)
# print(m)
for i in range(len(d)):
    k = d.get(c[i])

    print(str(m[i]) + ':', end=' ')
    for j in range(5):
        print(str(k[j]), end=' ')
    print()


# g = [[j for j in input().split(';')] for k in range(n)]
# print(g)

# a = []
# b = []
# for i in range(len(g)):
#     if i % 2 == 0:
#         a.append(g[i])
#     else:
#         b.append(g[i])

# print(a, b)
# win =
# lose =
# drow =
# score =
# win lose drow score


# for i in range(len(g)):
#     if int(int(g[i][1])) >  int(g[i][3]):
#         print(g[i][0])
#     if int(int(g[i][1])) ==  int(g[i][3]):
#         print('Ничья')
#     else:
#         print(g[i][2])


# h = [] # единый общий список команд и голов
# for i in range(n):
#     [h.append(x) for x in input().split(';')]