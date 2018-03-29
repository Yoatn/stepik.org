
import re
import sys

import requests
import re

# FirstLink = str(input()).rstrip()

# FirstLink = 'http://pastebin.com/raw/7543p0ns' # test 3
FirstLink = 'http://pastebin.com/raw/hfMThaGb' # test 2

res = requests.get(FirstLink)
print(res.text)

# if 'blogi.rbc.ru' in res.text:
#     print(True)

res1 = re.findall(r'href="[ftp|http].+?//(.+?ru|.+?org|.+?ge)', res.text)
# print(res1)
# TempleList = []


# for i in res1:
#     print(i)
#     # if 'drinktime.ru' in i:
#     #     print(i)
#     #     break
#     NewLink = re.findall(r'[ftp.|htt].+?//(.+?ru|.+?org|.+?ge)', i)
#     if NewLink:
#         # print(NewLink[0])
#         TempleList.append(NewLink[0])
#
#
res1 = sorted(set(res1))
# print(TempleList)
for i in res1:
    print(i)
# print(res.text + '1 ответ')
# print(res.content)