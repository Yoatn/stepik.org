# --------------------------------------------------
# Programm by Yoatn
#
# Start date   05.12.2017   11:43
# End date     05.12.2017   14:17
#  
# Description:
#Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
#
# Sample Input:
# blabla is a tandem repetition
# 123123 is good too
# go go
# aaa
# Sample Output:
# blabla is a tandem repetition
# 123123 is good too
# --------------------------------------------------

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(r"\b(\w+)\1\b", line):
        print(line)
