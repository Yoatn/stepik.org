#--------------------------------------------------
# Programm by Yoatn
#
# Start date   00.00.2017   00:00
# End date     00.00.2017   00:00
#  
# Description:
#
#--------------------------------------------------
import os.path
# i = 'njkyn.py'

# for current_dir, dirs, files in os.walk('.'):
#     if i in files:
#         print(current_dir, dirs)

x = os.listdir('1')
print(x)
y = os.listdir('./1/' + f'{x[0]}')
print(y)
for i in x:
    # if '.' not in i:
        # print(os.listdir('./1/' + f'{i}'))
    if '.py' in i:
        print(os.listdir(i))