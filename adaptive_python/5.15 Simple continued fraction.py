# --------------------------------------------------
# Programm by Yoatn
#
# Start date   09.01.2018    12:05
# End date     
#  
# Description:
#
# --------------------------------------------------

# import datetime
# print(datetime.datetime.now().strftime('%d.%m.%Y    %H:%M'))


def continued_fraction(dividend, divider, List):
    whole = dividend // divider
    rest = dividend % divider
    List.append(whole)
    if rest != 0:
        continued_fraction(divider, rest, List)
    return  List

a, b = 239, 30
# a, b = map(int, input().split('/'))

ListAnswer = []
print(*continued_fraction(a, b, ListAnswer))


# # a, b = 239, 30
#
# a, b = map(int, input().split('/'))
# while b:
#     print(a // b, end=' ')
#     a, b = b, a % b