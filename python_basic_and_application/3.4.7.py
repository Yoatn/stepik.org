# --------------------------------------------------
# Programm by Yoatn
#
# Start date   08.12.2017   15:54
# End date     10.12.2017   23:50
#  
# Description:
#Вашей программе на вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.
#
# Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
# <a href="../some_path/index.html">﻿.
#
# Сайты следует выводить в алфавитном порядке.
#
# Пример HTML файла:
#
# <a href="http://stepic.org/courses">
# <a href='https://stepic.org'>
# <a href='http://neerc.ifmo.ru:1345'>
# <a href="ftp://mail.ru/distib" >
# <a href="ya.ru">
# <a href="www.ya.ru">
# <a href="../skip_relative_links">
#
# Пример ответа:
#
# mail.ru
# neerc.ifmo.ru
# stepic.org
# www.ya.ru
# ya.ru

# --------------------------------------------------

import requests
import re

# FirstLink = str(input()).rstrip()

FirstLink = 'http://pastebin.com/raw/7543p0ns' # test 3
# # # FirstLink = 'http://pastebin.com/raw/hfMThaGb' # test 2
# # #
res = requests.get(FirstLink)
# print(res.text)

# if 'blogi.rbc.ru' in res.text:
#     print(True)
# restext = 'href=https://pa-stebin.com/raw/hfMThaGb'
# restext = 'href="ftp://mail-2.ru/distib"'
# restext = '<a href="bya-2.ru">'
# restext = 'href= "http://ftepic.org/courses" id="dfdf"'
# www.gtu.edu.ge/index_e.htm
# restext = '<a href="http://www.gtu.edu.ge/index_e.htm" target="_top">Georgian Technical University</a>'
# res1 = re.findall(r'href=["]*[ftp|http|https]*[://]*', restext)
# restext = "href='http://neerc.ifmo.ru:111'"
# restext = '<a title=test download="http://mest.com"; href="test.com" class="my test" style=>'
# restext = '<a href="http://valid1.com/redirect.cgi?http://valid2.ru'

# restext = '<a href="htt://stepic.org/courses">'
# restext = '<a href="https://stepic.org">'
# restext = '<a href="http://neerc.ifmo.ru:1345">'
# restext = '<a href="ftp://mail.ru/distib" >'
# restext = '<a href="ya.ru">'
# restext = '<a href="www.ya.ru">'
# restext = '<a href="../skip_relative_links">'

res1 = re.findall(r'<a.*href=[^ ]["\']*?[htpsf]*?[:/]*([\w\.\-\_]*\.\w{2,3}\b)', res.text)
# res1 = re.findall(r'<a.*href=[^ ]["\']*?[htpsf]*?[:/]*([\w\.\-\_]*?ua\b|[\w\.\-\_]*?com\b|[\w\.\-\_]*\.\w{2,3}|[\w\.\-\_]+org\b|[\w\.\-\_]+ge\b)', restext)
# print(res1)
# print(res2)
# TempleList = []


# for i in res1:
#     # print(i)
#     # if 'drinktime.ru' in i:
#     #     print(i)
#     #     break
#     NewLink = re.findall(r'[ftp|htt].+?//(.+?ru|.+?org|.+?ge)', i)
#     if NewLink:
#         # print(NewLink[0])
#         TempleList.append(NewLink[0])


# res1 = sorted(set(res1))
# print(TempleList)
# for i in res1:
#     print(i)
# print(res.text + '1 ответ')
print(res.content)

print('\n'.join(sorted(set(res1))))