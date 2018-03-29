# --------------------------------------------------
# Programm by Yoatn
#
# Start date   28.12.2017   17:31
# End date     28.12.2017   18:30
#  
# Description:
#На вход программе подаётся строка, содержащая слова, разделённые
# пробелом. Программа должна вывести статистику длин слов в полученной
# строке, от меньшей длины слова к большей (см. пример).
#
# Словом считается последовательность произвольных символов,
# окружённая пробелами либо границами строки. Заметьте, что знаки
# препинания также относятся к слову.
#
# Формат ввода:
# Одна строка, содержащая последовательности латинских символов и
# знаков препинания, разделённые пробелом.
#
# Формат вывода:
# Для каждой длины слова, встречающейся в исходной строке, нужно
# указать количество слов с такой длиной
# длина: количество
# Статистика должна выводиться в порядке увеличения длины.
#
# Sample Input:
# Beautiful is better than ugly. Explicit is better than implicit.
# Sample Output:
# 2: 2
# 4: 2
# 5: 1
# 6: 2
# 8: 1
# 9: 2
# --------------------------------------------------


# StrIn = 'Beautiful is better than ugly. Explicit is better than implicit.////'
# StrIn = ['Beautiful', 'is,', 'better', 'than', 'ugly.', 'Explicit', 'is', 'better', 'than', 'implicit..']
StrIn = input().strip().split()
# print(StrIn)
LenElementStrIn = [len(i) for i in StrIn]
# print(LenElementStrIn)
for i in set(sorted(LenElementStrIn)):
    # print(str(i) + ':', str(LenElementStrIn.count(i)))
    print(r"{0}: {1}".format(i, LenElementStrIn.count(i)))