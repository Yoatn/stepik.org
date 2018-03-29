#--------------------------------------------------
# Programm by Yoatn
#
# Start date   22.10.2017   20:30
# End date     23.10.2017   01:09
#  
# Description:
#
#--------------------------------------------------
import re

with open('dataset_3363_2.txt', 'r+') as f:
    for line in f:
        line = line.strip()
        # print(line)
        l = re.split('(\d+)', line)
        # print(l)
x, y, z = [], [], []

for i in range(1, len(l), 2):
    if i % 2 != 0:
        x.append(l[i])

for j in range(0, len(l), 2):
    if j % 2 == 0:
        y.append(l[j])

for i in range(len(x)):
    z.append(y[i] * int(x[i]))
# print(z)
z = ''.join(z)
print(z)

with open('www.txt', 'r+') as fn:
    fn.write(z)
    for line in fn:
        line = line.strip()
        # print(line)