# --------------------------------------------------
# Programm by Yoatn
#
# Start date   05.12.2017   09:43
# End date     05.12.2017   09:57
#  
# Description:
#Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\﻿".
# Sample Input:
# \w denotes word character
# No slashes here
# Sample Output:
# \w denotes word character
# --------------------------------------------------

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(r'\\', line):
        print(line)

# print(re.findall(r'\\', r'\wcvdv'))
# print(re.match(r'\\', r'\wcvdv'))