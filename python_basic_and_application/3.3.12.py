# --------------------------------------------------
# Programm by Yoatn
#
# Start date   05.12.2017   16:12
# End date     05.12.2017   16:35
#  
# Description:
#Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human"
# на подстроку "computer"﻿ и выведите полученные строки.
#
# Sample Input:
# I need to understand the human mind
# humanity
# Sample Output:
# I need to understand the computer mind
# computerity
# --------------------------------------------------

import sys
import re

# ---------- 1st solution ---------------
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.findall('human', line):
#         print(line.replace('human', 'computer'))
#     else:
#         print(line)

# ---------- 2nd solution ---------------
for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r'human', 'computer', line)
    print(line)



