# --------------------------------------------------
# Programm by Yoatn
#
# Start date   
# End date     
#  
# Description:
#
# --------------------------------------------------

import socket
req = 'Hello tcp'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 58304))
s.send(req.encode())
rsp = s.recv(1024)
s.close()


