#--------------------------------------------------
# Programm by Yoatn
#
#
# Version      Date of the end        Info
#   1.0          13.10.2017       Initial Version
#
#--------------------------------------------------



a = int(input())
b = int(input())
c = int(input())
d = int(input())

for z in range(c, d + 1):
    print('\t', z, end='')
print()
for i in range(a, b + 1):
    print(i, end='\t')
    for z in range(c, d + 1):

        for j in range(c, d + 1):
            print(i * z, end='\t')
            break
    print()

    '''It was very hard for me, but I did it!
    Someday I will remember this with smile'''