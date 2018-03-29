#--------------------------------------------------
# Programm by Yoatn
#
#
# Version          Date                Info
#   1.0          01.10.2017       Initial Version
#
#--------------------------------------------------

# a = int(input())
#
# if a == 1 and a == 21:



x = int(input())

word = 'программист'
end_1 = 'а'
end_2 = 'ов'

# 1 _
# 2 3 4 а
# 5 - 19  ов

a1 = list() # Окончание на 1
a1.append(1)
a1.append(21)
b1 = 21
# c1 = (111, 211, 311, 411, 511, 611, 711, 811, 911)
while b1 < 990:
    b1 += 10
    a1.append(b1)
a1.remove(111)
a1.remove(211)
a1.remove(311)
a1.remove(411)
a1.remove(511)
a1.remove(611)
a1.remove(711)
a1.remove(811)
a1.remove(911)

# Окончание на 2
a2 = list()
a2.append(2)
a2.append(22)
b2 = 22
while b2 < 1000:
    b2 += 10
    a2.append(b2)
a2.remove(112)
a2.remove(212)
a2.remove(312)
a2.remove(412)
a2.remove(512)
a2.remove(612)
a2.remove(712)
a2.remove(812)
a2.remove(912)

# Окончание на 3
a3 = list()
a3.append(3)
a3.append(23)
b3 = 23
while b3 < 990:
    b3 += 10
    a3.append(b3)
a3.remove(113)
a3.remove(213)
a3.remove(313)
a3.remove(413)
a3.remove(513)
a3.remove(613)
a3.remove(713)
a3.remove(813)
a3.remove(913)

# Окончание на 4
a4 = list()
a4.append(4)
a4.append(24)
b4 = 24
while b4 < 990:
    b4 += 10
    a4.append(b4)
a4.remove(114)
a4.remove(214)
a4.remove(314)
a4.remove(414)
a4.remove(514)
a4.remove(614)
a4.remove(714)
a4.remove(814)
a4.remove(914)


if 0 <= x <= 1000:
    if x in a1:
        print(str(x) + ' ' + word)
    elif x in a2:
        print(str(x) + ' ' + word + end_1)
    elif x in a3:
        print(str(x) + ' ' + word + end_1)
    elif x in a4:
        print(str(x) + ' ' + word + end_1)
    else:
        print(str(x) + ' ' + word + end_2)



