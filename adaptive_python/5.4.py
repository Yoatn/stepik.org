# --------------------------------------------------
# Programm by Yoatn
#
# Start date   20.12.2017   13:07
# End date     00.00.2017   00:00
#  
# Description:
#В римской системе счисления для обозначения чисел используются следующие символы (справа записаны числа, которым они соответствуют в десятичной системе счисления):
#
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# Будем использовать вариант, в котором числа 4, 9, 40, 90, 400 и 900 записываются как вычитание из большего числа меньшего: IV, IX, XL, XC, CD и CM, соответственно.
#
# Напишите программу, которая переводит число из римской в десятичную систему счисления.
#
# Формат ввода:
# Строка, содержащая число, закодированное в римской системе счисления. Гарантируется, что число меньше 4000.
#
# Формат вывода:
# Строка, содержащая число в десятичной системе счисления, соответствующее введённому.
#
# Sample Input 1:
# MCMLXXXIV
# Sample Output 1:
# 1984
# Sample Input 2:
# IX
# Sample Output 2:
# 9
# Sample Input 3:
# III
# Sample Output 3:
# 3
# --------------------------------------------------

# DictNumber1 = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
# DictNumber2 = {4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}

DictNumber1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
DictNumber2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
# print(DictNumber2.keys())

NumberIn = input().strip()
# NumberIn = 'MCMLXXXIV'
BuferList = []
BuferList2 = []
for i in NumberIn:
    BuferList.append(i)
# print(BuferList)
# print(DictNumber1[i], end=' ')


for i in range(len(BuferList) - 1, -1, -1):
    try:
        # print(BuferList[i], end=' ')
        x = BuferList[i - 1] + BuferList[i]
        # print(x)

        if x in DictNumber2:

            # print(DictNumber2[x])
            BuferList2.append(DictNumber2[x])
            # print(BuferList[i], 'Bi')
            # print(BuferList[i - 1], 'Bi-1')
            BuferList.remove(BuferList[i - 1])
            BuferList.remove(BuferList[i - 1])

        else:
            # print(DictNumber1[BuferList[i]])
            BuferList2.append(DictNumber1[BuferList[i]])
            BuferList.remove(BuferList[i])
    except IndexError:
        continue
print(str(sum(BuferList2)))