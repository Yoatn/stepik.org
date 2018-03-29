# --------------------------------------------------
# Programm by Yoatn
#
# Start date   11.01.2018   23:25
# End date     
#  
# Description:
#
# --------------------------------------------------
#
# import datetime
# print(datetime.datetime.now().strftime("%d.%m.%Y   %H:%M"))

import socket
import os
import sys

s = socket.socket # (socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

while 1:
    conn, addr = s.accept()
    child_pip = os.fork()
    if child_pip == 0:
        request = conn.recv(1024)
        conn.send(request.upper())
        print('(child {}) {} : {}'.format(conn.getpeername(), request))
        conn.close()
        sys.exit()
    else:
        conn.close()
    # while 1:
    #     data = conn.recv(1024)
    #     if not data or data == 'close': break
    #     conn.send(data)
    # conn.close()
s.close()