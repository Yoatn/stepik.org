#--------------------------------------------------
# Programm by Yoatn
#
# Start date   23.10.2017   21:47
# End date     24.10.2017   01:25
#  
# Description:
# Скачайте файл. В нём указан адрес другого файла, который нужно
#  скачать с использованием модуля requests и посчитать число строк в нём.
#
# Используйте функцию get для получения файла (имеет смысл вызвать
# метод strip к передаваемому параметру, чтобы убрать пробельные символы по краям).
#
# После получения файла вы можете проверить результат, обратившись
# к полю text. Если результат работы скрипта не принимается, проверьте поле
# url на правильность. Для подсчёта количества строк разбейте текст с помощью
# метода splitlines.
#
# В поле ответа введите одно число или отправьте файл, содержащий
# одно число.
# #--------------------------------------------------

import requests

print(len(requests.get('https://stepic.org/media/attachments/course67/3.6.2/316.txt').text.splitlines()))

# a = str(r)
# a = a.strip()
# a = list(a)
# r = r.strip()
# print(a)
# print(a.count('\n'))
# print(len()r)