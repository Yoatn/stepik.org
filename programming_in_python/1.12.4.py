#--------------------------------------------------
# Programm by Yoatn
#
#
# Version          Date                Info
#   1.0          01.10.2017       Initial Version
#
#--------------------------------------------------

import math


h = input()
if h == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(float(S))
if h == 'прямоугольник':
    a = int(input())
    b = int(input())
    S = a * b
    print(float(S))
if h == 'круг':
    r = int(input())
    pi = 3.14
    S = pi * (r ** 2)
    print(float(S))