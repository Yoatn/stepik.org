#--------------------------------------------------
# Programm by Yoatn
#
# Start date   00.00.2017   00:00
# End date     00.00.2017   00:00
#  
# Description:
#
#--------------------------------------------------

# DictIn = {'A': [], 'B': ['A', 'C'], 'C': ['A']} # Heir: Parents
# DictIn = {'B': ['A', 'C'], 'C': ['A'], 'A': [],
#           'D': ['C', 'F'], 'E': ['D'], 'F': []
#           }
# DictIn = {'A': ['B', 'C', 'D'], 'E': ['F', 'G'],
#           'I': ['E', 'F', 'Y', 'D', 'G'], 'B': ['I', 'Y', 'D', 'G'],
#           'F': ['D', 'Z'], 'C': ['Y', 'G', 'Z'], 'Y': [], 'D': [],
#           'G': ['Y', 'D'], 'Z': ['D', 'G']
#           }


def InvertParentHeir(DictIn):
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


    return InvDictOut

# print(InvertParentHeir(DictIn))