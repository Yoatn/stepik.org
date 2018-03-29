#--------------------------------------------------
# Programm by Yoatn
#
#
# Version          Date                Info
#   1.0          13.10.2017       Initial Version
#
#--------------------------------------------------

a = int(input())
b = int(input())

s, z = 0, 0

while a % 3 != 0:
    a += 1

for i in range(a, b + 1, 3):
    z +=1
    s += i

print(s / z)