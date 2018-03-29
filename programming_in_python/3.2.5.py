#--------------------------------------------------
# Programm by Yoatn
#
# Start date   21.10.2017   19:33
# End date     22.10.2017   01:55
#  
# Description:
# Напишите функцию update_dictionary(d, key, value), которая принимает на
# вход словарь d и два числа: key и value.
#
# Если ключ key есть в словаре d, то добавьте значение value в
# список, который хранится по этому ключу.
# Если ключа key нет в словаре, то нужно добавить значение в список по
# ключу 2⋅key. Если и ключа 2⋅key нет, то нужно добавить ключ
# 2⋅key в словарь и сопоставить ему список из переданного
# элемента[value].
#
# Требуется реализовать только эту функцию, кода вне неё не должно быть.
# Функция не должна вызывать внутри себя функции input и print.
#
# Пример работы функции:
#
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}
#--------------------------------------------------

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif 2 * key not in d:
        d[2 * key] = [value]
    elif key not in d:
        d[2 * key].append(value)

    return d.get(key)


d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)

# d = {1: [3], 4: [4]}
# a = 4
# b = 6
# update_dictionary(d, a, b)
# print(d)


# while len(d) < 2:
#     a, b = [x for x in input().split()]
#     update_dictionary(d, a, b)

# d.update({2 * key : [value]}) - добавляет в существующий список новую пару