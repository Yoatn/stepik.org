# --------------------------------------------------
# Programm by Yoatn
#
# Start date   12.11.2017   23:08
# End date     00.00.2017   00:00
#  
# Description:
#
# --------------- draft ----------------------------


import sys
sys.stdin = open("2.1.7.txt", "r")

def func(p, d):
    l = []
    for i in d:
        if p in d[i]:
            l.append(i)
            l.extend(func(i, d))
    return l


def invert_dict_nonunique(d):
    newdict = {}
    for k, v in d.items():
        newdict.setdefault(v, []).append(k)
    return newdict



DictParentHeir = {}
for i in range(int(input())):
    a = input()
    if ' : ' in a:
        n = a.split(' : ')
        DictParentHeir.setdefault(n[0], n[1].split(' '))
    else:
        DictParentHeir.setdefault(a, ['0'])
# print(DictParentHeir)
    #     DictParentHeir.setdefault(a, a)
# print(DictParentHeir, 'DictParentHeir')

# invert_dict = invert_dict_nonunique(DictParentHeir)
# print(invert_dict, 'invert_dict')

for i in DictParentHeir:
    DictParentHeir[i].sort()
print(DictParentHeir, 'sort DictParentHeir')
#
#
a = []

for q in range(int(input())):
    b = input()
    a.append(b)
print(a, 'a')
#
n = []
m = []
o = []
for j in a:
    # print(j, 'j')
    # print(func(j, DictParentHeir))
    n += (func(j, DictParentHeir))
    # print(n)
    try:
        for i in DictParentHeir[j]:
            # print(i, 'i')
            #             # print(invert_dict[j], 'invert_dict[j]')

            try:
                if j in n:

                    # if j not in n:


                    if j not in o:
                        print(j)
                    o.append(j)
            except (KeyError, ValueError):
                pass
    except (KeyError, ValueError):
        pass
print(o)