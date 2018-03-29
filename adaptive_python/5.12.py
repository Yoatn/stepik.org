# --------------------------------------------------
# Programm by Yoatn
#
# Start date   21.12.2017   22:57
# End date     00.00.2017   00:00
#  
# Description:
#
# --------------------------------------------------

import sys

for Command in sys.stdin:
    Command = Command.rstrip()

    if Command != 'End':
        print(f'Processing "{Command}" command...')
    else:
        print('Good bye!')
        break

