#--------------------------------------------------
# Programm by Yoatn
#
# Start date   24.10.2017   01:30
# End date     24.10.2017   02:07
#  
# Description:
#
#--------------------------------------------------

import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt').text
print(r)
a = '.txt'
c = 0
b = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r).text
print(b)
while a in b:
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + b).text
    c += 1
    print(r)
    print(c)
    b = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r).text
    c += 1
    print(b)
    print(c)


# if '.txt' in r:
