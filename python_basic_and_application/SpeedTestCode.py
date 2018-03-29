# --------------------------------------------------
# Programm by Yoatn
#
# Start date   00.00.2017   23:00
# End date     00.00.2017   00:00
#  
# Description:
#
# --------------------------------------------------

import time


class SpeedTest(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))

# with SpeedTest() as S:

#
#     import requests
#     import json
#
#     # FinalList = ['1974 Aberle Christian', '1952 Abell Jenny', '1977 Aasan Øystein',
#     #              '1967 Abts Tomma', '1887 Ackermann Max', '1959 Aaron Joseph', '1963 Ackermann Franz',
#     #              '1940 Abbott Angela', '1909 Abercrombie Gertrude', '1978 3TTMan', '1954 Abegg Jimmy',
#     #              '1947 Ackling Roger', '1803 Abbati Vincenzo', '1955 Ableton Miguel',
#     #              '1538 Abondio Antonio'
#     #              ]
#     FinalList = []
#
#     with open('dataset_24476_4.txt', 'r') as f:
#         for line in f:
#             NewLine = line.strip()
#             client_id = 'de7e3482fcea4aa2ab6c'
#             client_secret = 'b5d05534689887c60fd3e7bdd3d3c4fa'
#
#             # инициируем запрос на получение токена
#             r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
#                               data={
#                                   "client_id": client_id,
#                                   "client_secret": client_secret
#                               })
#
#             j = json.loads(r.text)
#
#             token = j["token"]
#
#             headers = {"X-Xapp-Token": token}
#             r = requests.get(f"https://api.artsy.net/api/artists/{NewLine}", headers=headers)
#             r.encoding = 'utf-8'
#
#             j = json.loads(r.text)
#             # print(j)
#
#             # print(j['birthday']+ ' ' + j['sortable_name'])
#
#             FinalList.append(j['birthday'] + ' ' + j['sortable_name'])
#     # print(FinalList)
#     sorted(FinalList)
#     SortNewList = sorted(FinalList)
#     print(SortNewList)
#     for i in SortNewList:
#         print(i[5:])