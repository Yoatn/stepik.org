#--------------------------------------------------
# Programm by Yoatn
#
#
# Version          Date                Info
#   1.0          04.10.2017       Initial Version
#
#--------------------------------------------------


a = int(input())

b = []

while a != 0:
    b.append(a)
    a = int(input())
    b.append(a)
    break
while a != 0:
    a = int(input())
    b.append(a)

print(sum(b))