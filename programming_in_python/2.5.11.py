#--------------------------------------------------
# Programm by Yoatn
#
# Start date   17.10.2017
# End date     00.00.2017
#  
# Description:
#
#--------------------------------------------------



# a = [1, 1, 1, 5, 1, 2, 2, 5, 3, 2, 4, 1]
a = [int(x) for x in input().split()]
a.sort()
b = []

if len(a) > 1:
    for i in range(0, len(a) - 1):
        if a[i] == a [i + 1]:
            b.append(a[i])
    else:
        print()
d = list(set(b))
for j in range(0, len(d)):
    print(d[j], end=' ')
