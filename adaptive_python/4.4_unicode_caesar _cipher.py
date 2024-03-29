# --------------------------------------------------
# Programm by Yoatn
#
# Start date   24.12.2017   10:33
# End date     24.12.2017   10:00
#  
# Description:
# Суть задачи та же, что и Caesar cipher, с одним
# отличием: кодируются символы из интервала 1F600—1F64F
# таблицы символов Юникода. Используется кодировка UTF-8.

# Для всех символов сдвиг один и тот же. Сдвиг
# циклический, т.е. если к последнему символу
# алфавита применить единичный сдвиг, то он заменится
#  на первый символ, и наоборот.
#
# Напишите программу, которая шифрует текст шифром
# Цезаря.
#
# Формат ввода:
# На первой строке указывается используемый сдвиг
# шифрования: целое число. Положительное число
# соответствует сдвигу вправо. На второй строке
# указывается непустая фраза для шифрования.
#
# Не обращайте внимания, если у вас отображаются
# прямоугольники вместо некоторых символов. Это
# значит, что ваш шрифт не содержит этих символов. Д
# ля решения задачи это не имеет никакого значения.
#
# Формат вывода:
# Единственная строка, в которой записана фраза:
# Result: "..." , где вместо многоточия внутри
# кавычек записана зашифрованная последовательность.
#
# Sample Input 1:
# 1
# 😀🙏😇
# Sample Output 1:
# Result: "😁😀😈"
# Sample Input 2:
# 1
# 😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟
# 😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾
# 😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏
# Sample Output 2:
# Result: "😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚
# 😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹
# 😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏😀"
# --------------------------------------------------


def CesarEncryptEng(PhraseIn, Shift):
    Alpha = '😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠 \
    😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆 \
    🙇🙈🙉🙊🙋🙌🙍🙎🙏'
    PhraseOut = [(Alpha[(Alpha.index(i) + Shift) % len(Alpha) ]) for i in PhraseIn]
    return(''.join(PhraseOut))
#
# # PhraseIn = 'abc'
# # PhraseIn = PhraseIn.lstrip(' ').rstrip(' ')
# # Shift = -57
# # o = Shift%-27
# # print(o)
# # # print()
# # # print(int(Shift - 2.7 * 10 * (Shift//27)))
# # # j = int(Shift - 2.7 * 10 * (Shift//27))
# # #
# # Alpha = ' abcdefghijklmnopqrstuvwxyz'
# # if Shift > 27:
# #     Shift = Shift%27
# # if Shift < -27:
# #     Shift = Shift%-27
# # print(Shift)
# # ShiftAlpha = Alpha[Shift:] + Alpha[:Shift]
# # print(ShiftAlpha)
# # PhraseOut = ''
# # for i in PhraseIn:
# #     PhraseOut += ShiftAlpha[Alpha.index(i)]
# # print(PhraseOut)
#
#
# #
# # PhraseIn = 'a'
# # Shift = 58
# #
if __name__ == '__main__':
    Shift = int(input())
    PhraseIn = input().strip()

    print('Result: ' + '"' + CesarEncryptEng(PhraseIn, Shift) + '"')

# Alpha = '😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏'
# print(Alpha[7])