#--------------------------------------------------
# Programm by Yoatn
#
# Start date   09.12.2017   11:00
# End date     09.12.2017   11:50
#  
# Description:
#Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.
#
# Одним из атрибутов преступления является его тип – Primary Type.
#
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
#
# Файл с данными:
# Crimes.csv
# #--------------------------------------------------

import csv

BufferList = []
n = 0

with open ('Crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if '2015' in row[2]:
            BufferList.append(row[5])
# print(BufferList)
SetBufferList = set(BufferList)

# print(SetBufferList)

Dict = {}

for i in SetBufferList:
    a = BufferList.count(i)
    Dict.setdefault(a, i)
    if a > n:
        n = a
print(Dict[n])

