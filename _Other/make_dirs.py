#--------------------------------------------------
# Programm by Yoatn
#
# Start date   25.11.2017   23:41
# End date     00.00.2017   00:00
#
# Description:
#
#--------------------------------------------------


import os
path = r'C:\Users\Alpina_13\Google Диск\Cloud\code\python\geekbrains\specializations\pyrhon_ part_1'

Lst = ['easy', 'normal', 'hard']

for i in range(1,9):
    path2 = path + f'\lesson0{i}\homework0{i}'
    os.makedirs(path2)
    for j in Lst:
        open(f'{path2}\hw0{i}_{j}.py', 'w')

