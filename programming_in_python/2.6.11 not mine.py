#--------------------------------------------------
# Programm by Yoatn
#
# Start date   18.10.2017   00:14
# End date     00.00.2017   00:00
#  
# Description:
#Выведите таблицу размером n×n, заполненную числами от 1 до n2
# по спирали, выходящей из левого верхнего угла и закрученной по
# часовой стрелке, как показано в примере (здесь n=5):

# Sample Input:
# 5
# Sample Output:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9
#--------------------------------------------------

n = int(input())
i, j = 0, -1
max_j, max_i = n - 1, n - 1
min_j, min_i = 0, 1
count = 1
mtrx = [[0 for j in range(n)] for i in range(n)]
while True:

    while j < max_j:
        j += 1
        mtrx[i][j] = count
        count += 1
    max_j -= 1
    while i < max_i:
        i += 1
        mtrx[i][j] = count
        count += 1
    max_i -= 1
    while j > min_j:
        j -= 1
        mtrx[i][j] = count
        count += 1
    min_j += 1
    while i > min_i:
        i -= 1
        mtrx[i][j] = count
        count += 1
    min_i += 1

    if j == (n - 1) // 2 and i == n // 2:
        break


for i in range(n):
    for j in range(n):
        print(mtrx[i][j], end=' ')
    print()