#--------------------------------------------------
# Programm by Yoatn
#
# Start date   03.12.2017   12:23
# End date     00.00.2017   00:00
#  
# Description:
#
#--------------------------------------------------

import requests
import re

# FirstLink = str(input()).rstrip()
# SecondLink = str(input()).rstrip()

FirstLink = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
SecondLink = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'

res = requests.get(FirstLink)
# print(res.text + '1 ответ')
# print(res.content)

res = re.findall(r'\"(https://.+?|http://.+?)\"', res.text)
# print(res)
res = ['https://stepic.org/media/attachments/lesson/24472/sample1.html', 'https://stepic.org/media/attachments/lesson/2/sample1.html']
# print(len(res))
a = []
for i in res:
#     # print(i)
#     # i = str(i)
#     # i = re.sub('["]', '', i)
#     # print(i)
    res1 = requests.get(i)
    res1 = re.findall(r'\"(https://.+?|http://.+?)\"', res1.text)
    # print(res1)
    for j in res1:
        a.append(j)
    print(a)
if SecondLink in a:
    print('Yes')
else:
    print('No')
# res1 = requests.get(res[0])
# # print(res1.text + '2 ответ')
#
# res1 = re.findall('https:.+html', res1.text)
#
# if SecondLink in res1:
#     print('Yes')
# else:
#     print('No')


# print(FirstLink, Seco