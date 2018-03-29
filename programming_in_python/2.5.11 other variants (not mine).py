#--------------------------------------------------
# Programm by Yoatn
#
# Start date   17.10.2017
# End date     00.00.2017
#  
# Description:
#
#--------------------------------------------------



ls = [int(i) for i in input().split()]
for i in set(ls):
    if ls.count(i) > 1:
        print(i, end=' ')
