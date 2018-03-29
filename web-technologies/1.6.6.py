# --------------------------------------------------
# Programm by Yoatn
#
# Start date   11.01.2018   18:24
# End date     
#  
# Description:
#
# --------------------------------------------------
#
# import datetime
# print(datetime.datetime.now().strftime("%d.%m.%Y   %H:%M"))


# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('0.0.0.0', 2222))
# s.listen(10)
# while 1:
#     conn, addr = s.accept()
#     while 1:
#         data = conn.recv(1024)
#         if not data or data == 'close': break
#         conn.send(data)
#     conn.close()

import socket
import os


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
pid = os.fork()
if pid == 0:
    while 1:
        conn, addr = s.accept()

        data = conn.recv(1024)

        conn.send(data)
        conn.close()