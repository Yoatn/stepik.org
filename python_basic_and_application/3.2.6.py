# --------------------------------------------------
# Programm by Yoatn
#
# Start date   30.11.2017   11:00
# End date     30.11.2017   16:33
#  
# Description:
#
# Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
# За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
#
# Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba", после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s﻿.
#
# Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a, либо же определить, что это невозможно.
#
# Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a.
# Если после применения любого числа операций в строке s останутся вхождения строки a, выведите Impossible.
# Sample Input 1:
# ababa
# a
# b
# Sample Output 1:
# 1
# Sample Input 2:
# ababa
# b
# a
# Sample Output 2:
# 1
# Sample Input 3:
# ababa
# c
# c
# Sample Output 3:
# 0
# Sample Input 4:
# ababac
# c
# c
# Sample Output 4:
# Impossible
#
# --------------------------------------------------

def replace(start_list, old_arg, new_arg, n):
    if old_arg in start_list and old_arg in new_arg:
        return 'Impossible'
    if old_arg in start_list:
        new_list = start_list.replace(old_arg, new_arg)
        n += 1
        return replace(new_list, old_arg, new_arg, n)
    else:
        return n

s, a, b = (input().strip() for i in range(3))
print(replace(s, a, b, 0))
