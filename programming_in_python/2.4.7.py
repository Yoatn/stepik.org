#--------------------------------------------------
# Programm by Yoatn
#
# Start date   13.10.2017
# End date     17.10.2017
#  
# Description:
#Узнав, что ДНК не является случайной строкой, только
# что поступившие в Институт биоинформатики студенты
# группы информатиков предложили использовать алгоритм
# сжатия, который сжимает повторяющиеся символы в строке.
#
# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть
# группы одинаковых символов исходной строки
# заменяются на этот символ и количество его повторений
# в этой позиции строки.
#
# Напишите программу, которая считывает строку, кодирует
# её предложенным алгоритмом и выводит закодированную
# последовательность на стандартный вывод. Кодирование
# должно учитывать регистр символов.
#
# Sample Input 1:
# aaaabbcaa
# Sample Output 1:
# a4b2c1a2
# Sample Input 2:
# abc
# Sample Output 2:
# a1b1c1
#--------------------------------------------------

# a = str(input())
# b = a + '0'
# alen = len(a)
#
# x= 0
# s = []
#
# while x < alen:
#     if a[x] == b[x + 1]:
#         s.append(a[x])
#     else:
#         s.append(a[x])
#         print(str(a[x]) + str(s.count(a[x])), end='')
#         s.clear()
#     x += 1

SrtIn = 'aaaabbcaa'
# SrtIn = input()
ListIn = [i for i in SrtIn]
print(ListIn)

