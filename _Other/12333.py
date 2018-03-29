#--------------------------------------------------
# Programm by Yoatn
#
# Start date   00.00.2017   00:00
# End date     00.00.2017   00:00
#  
# Description:
#
#--------------------------------------------------
a = []
while True:
  lst = str(input())
  if lst == 'end' :
    break
  a.append([i for i in lst.split()])

print(a, len(a))
