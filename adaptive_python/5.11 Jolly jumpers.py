# --------------------------------------------------
# Programm by Yoatn
#
# Start date   08.01.2018   22:57
# End date     08.01.2018   23:57
#  
# Description:
#Последовательность n>0 целых чисел называется
# jolly jumper в случае, если значения абсолютных
# разностей последовательных элементов принимают
# все возможные значения между 1 и n−1.
#
# Например, последовательность 1 -3 -4 -1 1
# является jolly jumper последовательностью,
# так как абсолютные разности равны 4 1 3 2,
# соответственно, а n−1=4.
# Будем считать, что последовательность из
# одного числа является jolly jumper.
#
# Напишите программу, которая проверяет,
# является ли введённая последовательность
# jolly jumper.
#
# Формат ввода:
#
# Строка, содержащая 1≤n≤100001
# целых чисел, разделённых пробелом.
#
# Формат вывода:
# Одна строка, содержащая "Jolly" (без кавычек),
# если последовательность является jolly
# jumper и "Not jolly" в противном случае.
#
# Sample Input 1:
# 1 -3 -4 -1 1
# Sample Output 1:
# Jolly
# Sample Input 2:
# 1 3 5
# Sample Output 2:
# Not jolly
# Sample Input 3:
# 4
# Sample Output 3:
# Jolly
# --------------------------------------------------
#
import datetime
print(datetime.datetime.now().strftime('%d.%.%Y    %H:%M'))

# import math

# In = [1, -3, -4, -1, 1]
# In = [1, 3, 5]
# In = [int(i) for i in input().split()]
# AbslVal = [(abs(In[i] - In[i - 1])) for i in range(1, len(In))]
#
# AbslVal = sorted(AbslVal)
#
# if AbslVal == [i for i in range(1, len(In))]:
#     print('Jolly')
# else:
#     print('Not jolly')