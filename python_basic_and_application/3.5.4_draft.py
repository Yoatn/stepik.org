
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x in seen:
            continue
        seen.add(x)
        result.append(x)
    return result

def func(p, d):
    l = []
    for i in d:
        if p in d[i]:
            l.append(i)
            l.extend(func(i, d))
    return unique(l)




# DictIn = {'A': [], 'B': ['A', 'C'], 'C': ['A']}
# DictIn = {'B': ['A', 'C'], 'C': ['A'], 'A': [],
#           'D': ['C', 'F'], 'E': ['D'], 'F': []
#           }
# DictIn = {'A': ['B', 'C', 'D'], 'E': ['F', 'G'],
#           'I': ['E', 'F', 'Y', 'D', 'G'], 'B': ['I', 'Y', 'D', 'G'],
#           'F': ['D', 'Z'], 'C': ['Y', 'G', 'Z'], 'Y': [], 'D': [],
#           'G': ['Y', 'D'], 'Z': ['D', 'G']
#           }


InvDictOut = {}

for i in DictIn: #
    # print(i)

    if i not in InvDictOut:
        InvDictOut.setdefault(i, [])
    if DictIn[i]:
        for j in DictIn[i]:
            if j not in InvDictOut:
                InvDictOut.setdefault(j, []).append(i)
            else:
                InvDictOut[j] += i


print(InvDictOut)
# for i in DictIn:
#     if i not in InvDictOut:
#         InvDictOut.setdefault(i, [])

# print(InvDictOut)



# for i in InvDictOut:
#     print(i)
#     NewInvDictOut.setdefault(i, unique(InvDictOut[i]))

# print(NewInvDictOut)


# for i in DictOut:
#     print(i, func(i, DictOut))
FinalList = []

for i in DictIn:
    x = i + ' : ' + str((len(func(i, DictIn)) +1))
    FinalList.append(x)

for i in sorted(FinalList):
    print(i)