#--------------------------------------------------
# Programm by Yoatn
#
# Start date   18.10.2017   17:02
# End date     00.00.2017   17:28
#  
# Description:
# Напишите программу, которая считывает список чисел lstlst из первой строки
#  и число xx из второй строки, которая выводит все позиции, на которых
# встречается число xx в переданном списке lstlst.
# Позиции нумеруются с нуля, если число xx не встречается в списке, вывести
# строку "Отсутствует" (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку,
# по возрастанию абсолютного значения.
#
#--------------------------------------------------



a = [int(x) for x in input().split()]
b = int(input())
# a = [1, 2, 5, 3, 6, 5, 1, 8, 6]
# b = 12

for i in range(len(a)):
    if b == a[i] and b in a:
        print(i, end=' ')
    if b not in a:
        print('Отсутствует')
        break




