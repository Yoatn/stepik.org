# --------------------------------------------------
# Programm by Yoatn
#
# Start date   12.11.2017   23:08
# End date     18.11.2017   11:40
#  
# Description:
#
# ---------------- main ---------------------------

# -------------- for tests --------------------
import sys
sys.stdin = open("2.1.7.txt", "r")

# -------------- main code --------------------
def func(p, d):
    l = []
    for i in d:
        if p in d[i]:
            l.append(i)
            l.extend(func(i, d))
    return l

DictParentHeir = {}
for i in range(int(input())):
    a = input()
    if ' : ' in a:
        n = a.split(' : ')
        DictParentHeir.setdefault(n[0], n[1].split(' '))
    else:
        DictParentHeir.setdefault(a, [])

a = []
for q in range(int(input())):
    b = input()
    a.append(b)

n = []
o = []
for j in a:
    n += (func(j, DictParentHeir))
    try:
        for i in DictParentHeir[j]:
            try:
                if j in n:
                    if j not in o:
                        print(j)
                o.append(j)
            except (KeyError, ValueError):
                pass
    except (KeyError, ValueError):
        pass

# -------------- the end main code --------------------