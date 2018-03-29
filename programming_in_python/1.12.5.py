#--------------------------------------------------
# Programm by Yoatn
#
#
# Version          Date                Info
#   1.0          01.10.2017       Initial Version
#
#--------------------------------------------------


a = int(input())
b = int(input())
c = int(input())

m = [a, b, c]

maximum = max(m)
minimum = min(m)

m.remove(maximum)
m.remove(minimum)

print(maximum)
print(minimum)
print(m[0])


# ----------- 11.11.17 ------------------

m = [int(input()) for i in range(3)]
m.sort()
print(max(m), min(m), m[1], sep='\n')
