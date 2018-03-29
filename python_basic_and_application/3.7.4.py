# --------------------------------------------------
# Programm by Yoatn
#
# Start date   13.12.2017   10:52
# End date     00.00.2017   00:00
#  
# Description:
#Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
#
# Пример:
#
# <cube color="blue">
#   <cube color="red">
#     <cube color="green">
#     </cube>
#   </cube>
#   <cube color="red">
#   </cube>
# </cube>
#
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий
# корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним,
# имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.
#
# Ценность цвета равна сумме ценностей всех кубиков этого цвета.
#
# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
# Sample Input:
# <cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
# Sample Output:
# 4 3 1
# --------------------------------------------------

from xml.etree import ElementTree


def color_rec_func(root, level=1):
    if root.findall('cube'):
        for i in root.findall('cube'):
            color_rec_func(i, level + 1)
    colors[root.attrib['color']] += level


colors = {'red': 0, 'green': 0, 'blue': 0}

# a = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'

tree =  ElementTree.fromstring(input())
color_rec_func(tree)
print(colors['red'], colors['green'], colors['blue'])