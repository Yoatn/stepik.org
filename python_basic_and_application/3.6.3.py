#--------------------------------------------------
# Programm by Yoatn
#
# Start date   09.12.2017   19:48
# End date     09.12.2017   20:45
#  
# Description:
#
#--------------------------------------------------

import requests


with open('dataset_24476_3.txt', 'r') as f:
    for line in f:
        NewLine = line.strip()
        # print(line)
        # Number = int(input())
        # Number = 1111

        api_url = f'http://numbersapi.com/{NewLine}/math'

        params = {
            'json': 'true'
        }

        # headers = {'Content-type': 'application/json',  # Определение типа данных
        #            'Accept': 'text/plain',
        #            'Content-Encoding': 'utf-8'}

        res = requests.get(api_url, params=params)
        # print(res.status_code)
        # print(res.headers['Content-Type'])
        # print(res.json())

        # data = res.json()
        # Found = res.json()['found']
        # print(data['found'])

        if res.json()['found']:
            print('Interesting')
        else:
            print('Boring')
