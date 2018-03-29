#--------------------------------------------------
# Programm by Yoatn
#
# Start date   21.10.2017   00:54
# End date     21.10.2017   15:01
#  
# Description:
#апишите функцию modify_list(l), которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать, требуется только изменение
# переданного списка, например:

# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
# Функция не должна осуществлять ввод/вывод информации.
#--------------------------------------------------

def modify_list(l):
    x = len(l)

    for i in range(-x, -1):
        if l[i] % 2 != 0:
            l.remove(l[i])

    x = len(l)
    for i in range(x):
        if l[i] % 2 != 0:
            l.remove(l[i])

    x = len(l)
    for j in range(x):
        l[j] /= 2
        l[j] = int(l[j])

    # x = len(l) - 1
    # while l.count(0) > 0:
    #     if l[x] == 0:
    #         l.remove(l[x])
    #     x -= 1
# Это условие нужно чтобы убрать нули из вывода.
    return l


lst = [0, 0, 0, 8, 1, 5, 0, 4, 100, 235, 18]
modify_list(lst)
print(lst)

