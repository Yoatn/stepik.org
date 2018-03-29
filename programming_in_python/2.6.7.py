#--------------------------------------------------
# Programm by Yoatn
#
# Start date   18.10.2017
# End date     18.00.2017
#  
# Description:
#
#--------------------------------------------------

a = [int(input())]

while sum(a) != 0:
    a.append(int(input()))
print(sum(i ** 2 for i in a))