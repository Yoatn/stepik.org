# --------------------------------------------------
# Programm by Yoatn
#
# Start date   04.12.2017   15:43
# End date     04.12.2017   16:25
#  
# Description:
#Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.
#
# Примечание:
# Для работы со словами используйте группы символов \b и \B.
# Описание этих групп вы можете найти в документации.
# Sample Input:
# cat
# catapult and cat
# catcat
# concat
# Cat
# "cat"
# !cat?
# Sample Output:
# cat
# catapult and cat
# "cat"
# !cat?
# --------------------------------------------------
# --------------- main -----------------
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(r'\bcat\b', line):
        print(line)
# --------------- the end main code -----------------
    if line == '***':
        break

