# --------------------------------------------------
# Programm by Yoatn
#
# Start date   16.12.2017   13:59
# End date     16.12.2017   14:05
#  
# Description:
#Задача на работу со строками.
# # Многим знакома детская загадка:
#
# А и Б сидели на трубе.
# А упало, Б пропало.
# Что осталось на трубе?
#
# Перевод, (какой я смог найти):
#
# A and B sat in the tree.
# A had fallen, B was stolen.
# What's remaining in the tree?
#
# Напишите программу, которая считывает два имени и выводит стихотворение, в котором вместо A и B используются эти имена.
#
# Формат ввода:
# Два имени, разделённых переносом строки. Первое имя должно заменять A, второе −− B.
#
# Формат вывода:
# Три строки стихотворения с заменёнными A и B.
#
# Sample Input:
# X
# Y
# Sample Output:
# X and Y sat in the tree.
# X had fallen, Y was stolen.
# What's remaining in the tree?
# --------------------------------------------------
#
a, b = input(), input()

print(f'{a} and {b} sat in the tree.\n'
      f'{a} had fallen, {b} was stolen.\n'
      'What\'s remaining in the tree?')



poem = ('{0} and {1} sat in the tree.\n'
        '{0} had fallen, {1} was stolen.\n'
        'What\'s remaining in the tree?')

print(poem.format(input(), input()))