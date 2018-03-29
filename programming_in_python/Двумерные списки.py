#--------------------------------------------------
# Programm by Yoatn
#
# Start date   17.10.2017
# End date
#
# Description: Разные варианты построения двумереых
# списков
#
#--------------------------------------------------

n = 4
a = [[0] * n] * n
a[0][0] = 5
print(a) #Создаёться один объект a на котрорый потом ссылаються все строчки n раз

b = [[0] * n for i in range(n)]
b[0][0] = 3
print(b) # Первый вариант создания независимого двумерного списка

c = [[0 for z in range(n)] for x in range(n)]
c[2][0] = 3
print(c) # Второй вариант создания независимого двумерного списка

f = len(c)
g = len(c[0])
for v in range(f):
    for w in range(g):
        print(c[v][w], end='')
    print() # Записть двумерного списка в матричном виде