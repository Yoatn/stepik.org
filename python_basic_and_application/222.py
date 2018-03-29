

a = ['z', 'o', 'a', 'f']
x = {'a': 'a', 'o': 'o'}
d = {'a': ['a'], 'o': ['o']}
# print(d['c'])
# print(d['b'])
n = []
for j in a:
    print(j, end='')
    try:
        for i in d[j]:
            print(i, end=' ')
            if i in a and a.index(j) > a.index(i):

                if j not in n:
                    n.append(j)
                    print(j)
    except KeyError:
        continue

