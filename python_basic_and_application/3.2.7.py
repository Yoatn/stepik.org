# --------------------------------------------------
# Programm by Yoatn
#
# Start date   30.11.2017   16:41
# End date     30.11.2017   17:00
#  
# Description:
#
# --------------------------------------------------

# s = "abababa"
# t = "aba"
#
# def finder(myStr, findStr):#Возвращает все вхождения подстроки findStr в строку myStr
#     mas = []
#     pos = 0
#     while pos != -1:
#         pos = myStr.find(findStr, pos)
#         mas += [pos]
#     return mas
#
# print(finder(s, t))

# StrIn = "abababa"
# el = "aba"
StrIn, el = input(), input()

loc = 0
Count = 0

while loc != -1:
    loc = StrIn.find(el)
    if loc >= 0:
        Count += 1
    StrIn = StrIn[loc+1:]
print(Count)

# print(s.find(''))