#--------------------------------------------------
# Programm by Yoatn
#
# Start date   18.10.2017   17:30
# End date     20.10.2017   00:03
#  
# Description:
# Напишите программу, на вход которой подаётся прямоугольная матрица
# в виде последовательности строк, заканчивающихся строкой,
# содержащей только строку "end" (без кавычек)
# Программа должна вывести матрицу того же размера, у которой
# каждый элемент в позиции i, j равен сумме элементов первой матрицы
# на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних
# символов соседний элемент находится с противоположной стороны матрицы.
# В случае одной строки/столбца элемент сам себе является соседом по
# соответствующему направлению.
#Sample Input 1:
# 9 5 3
# 0 7 -1
# -5 2 9
# end
# Sample Output 1:
# 3 21 22
# 10 6 19
# 20 16 -1
# Sample Input 2:
# 1
# end
# Sample Output 2:
# 4
# --------------------------------------------------


a = [x for x in input().split()]
b = []
b.append(a)
c = ['end']
while c not in b:
    a = [x for x in input().split()]
    b.append(a)

b.remove(c)
# print(b)

z = len(b)
y = len(b[0])

# print(z)
# print(y)
zlc = []
zlr = []

ps1, ps2, ps3, ps4 = 0, 0, 0, 0

for i in range(z):
    for j in range(len(b[i])):
        p1 = b[i][j - (y - 1)]
        p2 = b[i - (z - 1)][j]
        p3 = b[i][j - 1]
        p4 = b[i - 1][j]

        pss, ps1, ps2, ps3, ps4 = 0, 0, 0, 0, 0

        ps1 += int(p1)
        ps2 += int(p2)
        ps3 += int(p3)
        ps4 += int(p4)
        pss = ps1 + ps2 + ps3 + ps4

        zlc.append(pss)

        # print(p1, end=' ')
        # print(p2, end=' ')
        # print(p3, end=' ')
        # print(p4, end=' ')
        # print(pss)

    zlr.append(zlc)
    # print(zlc)
    zlc = []
print(zlr)

for i in range(len(zlr)):
    for j in range(len(zlr[i])):
        print(int(zlr[i][j]), end=' ')
    print()
