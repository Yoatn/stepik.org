# --------------------------------------------------
# Programm by Yoatn
#
# Start date   04.12.2017   16:20
# End date     04.12.2017   16:35
#  
# Description:
#Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
# Sample Input:
# zabcz
# zzz
# zzxzz
# zz
# zxz
# zzxzxxz
# Sample Output:
# zabcz
# zzxzz
# --------------------------------------------------

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(r'z.{3}z', line):
        print(line)