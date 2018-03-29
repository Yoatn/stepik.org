# --------------------------------------------------
# Programm by Yoatn
#
# Start date   20.11.2017   19:34
# End date     20.11.2017   20:11
#  
# Description:
# Реализуйте класс PositiveList, отнаследовав его от класса list, для
# хранения положительных целых чисел.
# Также реализуйте новое исключение NonPositiveError.
#
# В классе PositiveList переопределите метод append(self, x) таким образом,
# чтобы при попытке добавить неположительное целое число бросалось исключение
# NonPositiveError и число не добавлялось, а при попытке добавить положительное
# целое число, число добавлялось бы как в стандартный list.
#
# В данной задаче гарантируется, что в качестве аргумента x метода append всегда
# будет передаваться целое число.
#
# Примечание:
# Положительными считаются числа, строго большие ﻿нуля.
# -------------- main -----------------------------

class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
            return self
        else:
            raise NonPositiveError

# ------------ test --------------------
x = PositiveList()
x.append(4)
print(x)
x.append(-4)
print(x)
x.append(3)
print(x)
