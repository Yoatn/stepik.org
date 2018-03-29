# --------------------------------------------------
# Programm by Yoatn
#
# Start date   27.11.2017   12:00
# End date     27.11.2017   12:35
#  
# Description:
# Целое положительное число называется простым, если оно имеет ровно два различных делителя,
# то есть делится только на единицу и на само себя.
# Например, число 2 является простым, так как делится только на 1 и 2. Также простыми являются,
# например, числа 3, 5, 31, и еще бесконечно много чисел.
# Число 4, например, не является простым, так как имеет три делителя – 1, 2, 4. Также простым
# не является число 1, так как оно имеет ровно один делитель – 1.
#
# Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке
# возрастания, начиная с числа 2.
#
# Пример использования:﻿
#
# print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
#
# --------------------------------------------------



import itertools
# ------------- main code ---------------------
import math




def primes():
    x = 1
    while 1:
        x += 1
        if x > 1 and (math.factorial(x - 1) + 1) % x == 0:
            yield x
# ------------- Thr end main code ---------------------

# for i in primes():
#     if i < 33:
#         print(i)

print(list(itertools.takewhile(lambda x : x <= 31, primes())))