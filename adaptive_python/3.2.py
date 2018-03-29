# --------------------------------------------------
# Programm by Yoatn
#
# Start date   20.12.2017   20:34
# End date     20.12.2017   20:42
#  
# Description:
#
# --------------------------------------------------


def equation(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return -x / 2
    else:
        return (x - 2) ** 2 + 1

while 1:
    print(equation(float(input())))