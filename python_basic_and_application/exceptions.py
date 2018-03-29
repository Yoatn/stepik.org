# --------------------------------------------------
# Programm by Yoatn
#
# Start date   00.00.2017   23:00
# End date     00.00.2017   00:00
#  
# Description:
#
# --------------------------------------------------

class BadName(Exception):
    pass

def greet(name):
    if name[0].isupper():
        return 'Hello, ' + name
    else:
        raise BadName(name + ' is inapproriate name')