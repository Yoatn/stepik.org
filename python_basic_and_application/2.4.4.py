#--------------------------------------------------
# Programm by Yoatn
#
# Start date   25.11.2017   16:34
# End date     00.00.2017   16:57
#  
# Description:
#
#--------------------------------------------------

ListBaffer = []

with open('dataset_24465_4.txt', 'r') as f:
    for line in f:
        line = line.splitlines()
        ListBaffer.append(line[0])

ListBaffer.reverse()
# print(ListBaffer)

with open('dataset_24465_4.txt', 'w') as f:
    for i in ListBaffer:
        f.write(i + '\n')

