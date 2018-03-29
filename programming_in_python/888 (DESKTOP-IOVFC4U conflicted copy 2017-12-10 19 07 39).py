#--------------------------------------------------
# Programm by Yoatn
#
# Start date   00.00.2017   00:00
# End date     00.00.2017   00:00
#  
# Description:
#
#--------------------------------------------------

import re

# Line = '<a href="http://stepic.org/courses">'
# Line = '<a href="ftp://www.mya.ru">'
# Line = '<a href="../skip_relative_links">'

# Line = 'a href="http://www.cnews.ru/cgi-bin/redirect.cgi?http://corp.cnews.ru/'

# Line = '<a href="http://drinktime.ru">DrinkTime.ru</a>'

# Line = 'http://drinktime.ru'
# Line = '<a href="http://stepic.org/courses">'
# Line = '<a class = '"hello" 'href= "http://ftepic.org/courses" id="dfdf">'
# Line = '<p class = '"hello" 'href= '"http://dtepic.org/courses"
# Line = '<a class = '"hello" 'href = '"http://a.b.vc.ttepic.org/courses"
# Line = '<a href=\'https://stepic.org'
# Line = '<a href=\'http://neerc.ifmo.ru:1345'
# Line = '<a href = \'"ftp://mail.ru/distib" >'
# Line = '<a href= \'"ya.ru">'
Line = '<a href="bya-2.ru">'
# Line = '<a href="../skip_relative_links">'
# Line = '<link rel="image_src" href="https://examaple.org/files/6a2/72d/e09/6a272de0944f447fb5972c44cc02f795.png" '

print(re.findall(r'[href=]*?["]*?[ftp|http]+?.+?(.+?ru|.+?org|.+?ge)', Line))