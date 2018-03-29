#--------------------------------------------------
# Programm by Yoatn
#
# Start date   12.12.2017   10:43
# End date     12.12.2017   23:30
#  
# Description:
#Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
#
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
#
# ﻿Эквивалент на Python:
#
# class A:
#     pass
#
# class B(A, C):
#     pass
#
# class C(A):
#     pass
#
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.
#
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
#
# <имя класса> : <количество потомков>
#
# Выводить классы следует в лексикографическом порядке.
#
# Sample Input:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# Sample Output:
# A : 3
# B : 1
# C : 2
#--------------------------------------------------

import json

def unique_value_list(Lst): # Удаляет повторяющиеся значения в списке
    buffer = set()
    NewList = []
    for i in Lst:
        if i in buffer:
            continue
        buffer.add(i)
        NewList.append(i)
    return NewList


def find_heir_func(Parent, Dict): # Рекурсивный поиск потомков + unique_value_list
    Lst = []
    for i in Dict:
        if Parent in Dict[i]:
            Lst.append(i)
            Lst.extend(find_heir_func(i, Dict))
    return unique_value_list(Lst)


data = json.loads(input())

DictIn = {} # Формируем словарь {Потомок: Родители}

for i in data:
    DictIn.setdefault(i['name'], i['parents'])

FinalList = [] # Формируем список с элементами [Родитель : Количество потомком]

for i in DictIn:
    x = i + ' : ' + str((len(find_heir_func(i, DictIn)) + 1)) # +1 т.к. наследуемся от Object
    FinalList.append(x)

for i in sorted(FinalList): # Выводим построчно начения в отсортированном списке
    print(i)



