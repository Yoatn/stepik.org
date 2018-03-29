#--------------------------------------------------
# Programm by Yoatn
#
# Start date   00.00.2017   00:00
# End date     00.00.2017   00:00
#  
# Description:
#
#--------------------------------------------------

import requests

api_url = 'http://api.openweathermap.org/data/2.5/weather'

params = {
    'q': 'Moscow',
    'appid': '11c0d3dc6093f7442898ee49d2430d20'
}

res = requests.get(api_url, params=params)
print(res.status_code)
print(res.headers['Content-Type'])