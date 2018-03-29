# --------------------------------------------------
# Programm by Yoatn
#
# Start date   22.12.2017   19:07
# End date     00.00.2017   00:00
#  
# Description:
#
# --------------------------------------------------


import requests

Link = 'https://drive.google.com/drive/folders/0B86_efRBhbqpQkRHRDNZV2s0dlU'

res = requests.get(Link)
print(res.content)