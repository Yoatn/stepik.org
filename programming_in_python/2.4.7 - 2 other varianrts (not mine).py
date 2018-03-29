#--------------------------------------------------
# Programm by Yoatn
#
# Start date   13.10.2017
# End date     17.10.2017
#  
# Description:
#
#--------------------------------------------------





a = str(input()) # variant №1
l = len(a)
x = 1

for i in range(0, l):
    if i < (l - 1) and (a[i] == a[i + 1]):
        x += 1
    else:
        print(a[i], x, sep='', end='')
        x = 1

print()

# variant №2
import itertools
print("".join([k+str(len(list(g))) for k, g in itertools.groupby(a)]))



# variant №3
import re
print(re.sub(r'(.)(\1)+|(.)', lambda m: m.group(0)[0] + str(len(m.group(0))), a))