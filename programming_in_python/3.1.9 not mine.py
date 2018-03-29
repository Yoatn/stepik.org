#--------------------------------------------------
# Programm by Yoatn
#
# Start date   00.00.2017   00:00
# End date     00.00.2017   00:00
#  
# Description:
#
#--------------------------------------------------

def modify_list(l):
    l[:] = [i//2 for i in l if not i % 2]

    return l

a = [0, 0, 0, 8, 1, 5, 0, 4, 100, 235, 18]
modify_list(a)
print(a)