# --------------------------------------------------
# Programm by Yoatn
#
# Start date   07.01.2018   14:32
# End date     
#  
# Description:
# Напишите программу, которая выводит nn первых
# элементов последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно).
#
# Формат ввода:
# Строка, содержащая одно целое число nn, n>0n>0.
#
# Формат вывода:
# Строка, содержащая требуемую последовательность
# чисел, разделённых пробелом.
#
# Sample Input:
# 7
# Sample Output:
# 1 2 2 3 3 3 4
# --------------------------------------------------
#
# from time import gmtime, strftime
# print(strftime('%d.%m.%Y   %H:%M', gmtime()))


# In = int(input()) # solution 1
# In = 4
# Lst = []
# n = 1
#
# # while n <= (len(Lst) + 1):
# for j in range(In+1):
#     for i in range(j):
#         print(j, end=' ')
#         n += 1
#         if i == In:
#             break

# In = int(input()) # solution 2
# # In = 3
# n = 0
# for j in range(In+1):
#     for i in range(j):
#         if n == In:
#             break
#         print(j, end=' ')
#         n += 1

import math # solution 3
# In = int(input())
In = 3
print(*[math.ceil(((8*i + 1)**0.5-1)/2) for i in range(1, In + 1)])