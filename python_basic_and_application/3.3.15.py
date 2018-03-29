# --------------------------------------------------
# Programm by Yoatn
#
# Start date   07.12.2017   10:57
# End date     07.12.2017   18:01
#  
# Description:
#Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких
# одинаковых букв на одну букву.
# Буквой считается символ из группы \w.
# Sample Input:
# attraction
# buzzzz
# Sample Output:
# atraction
# buz
# --------------------------------------------------

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
# line = 'attraction, buzzzz'
    print(re.sub(r'((\w)\2+)', r'\2', line))