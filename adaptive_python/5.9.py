# --------------------------------------------------
# Programm by Yoatn
#
# Start date   22.12.2017   16:31
# End date     22.12.2017   18:30
#  
# Description:
#Fizz Buzz -- это классическая задача на программирование. Вот её немного изменённое условие.
#
# Напишите программу, которая принимает на вход два целых числа: начало и конец отрезка
# (оба числа входят в отрезок).
#
# Программа должна вывести числа из этого отрезка, но если число делится на 3, то вывести
# вместо него Fizz, если число делится на 5, вывести вместо него Buzz, а если делится и
# на три, и на 5, то вывести вместо этого числа FizzBuzz.
#

# Формат ввода:
# Два целых числа через пробел.
#
# Формат вывода:
# На отдельной строке каждое число из отрезка или слово, его заменяющее.
#
# Sample Input:
# 8 16
# Sample Output:
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# --------------------------------------------------


a, b = map(int, input().split(' ')) # solution #1 mine

for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 != 0:
        print('Fizz')
    elif i % 5 == 0 and i % 3 != 0:
        print('Buzz')
    elif i % 15 == 0:
        print('FizzBuzz')
    else:
        print(i)

a, b = map(int, input().split(' ')) # solution #2 not mine
for i in range(a, b + 1):
   print('Fizz' *(i % 3 == 0) + 'Buzz' *(i % 5 == 0) or i)

a, b = map(int, input().split(' ')) # solution #3 not mine
print(*['Fizz' *(i % 3 == 0) + 'Buzz' *(i % 5 == 0) or i for i in range(a, b + 1)], sep='\n')