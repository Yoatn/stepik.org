#--------------------------------------------------
# Programm by Yoatn
#
# Start date   23.10.2017   11:13
# End date     23.10.2017   14:54
#  
# Description:
# Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
#
# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
#
# Слова, написанные в разных регистрах, считаются одинаковыми.
#
# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
# Sample Output:
# abc 3
#
#--------------------------------------------------
import re

m = []
with open('dataset_3363_3.txt', 'r+') as f:
    for line in f:
        line = line.strip().lower()
        l = re.split(' ', line)
        m += l

d = {}
# for i in range(len(m)):
#     m[i] = m[i].lower()
m = sorted(m, reverse= True)
for i in range(len(m)):
    k = m[i]
    v = m.count(m[i])
    d.setdefault(k, v)

inv_d = {v: k for k, v in d.items()}
g = inv_d[max(inv_d)] + ' ' + str(max(inv_d))
print(g)

with open('dataset_3363_4.txt', 'r+') as f:
    f.write(g)



