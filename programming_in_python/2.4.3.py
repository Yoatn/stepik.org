#--------------------------------------------------
# Programm by Yoatn
#
#
# Version          Date                Info
#   1.0          13.10.2017       Initial Version
#
#--------------------------------------------------

a = input().lower()

z = a.count('c')
x = a.count('g')
y = len(a)
print(((z + x) / y) * 100)