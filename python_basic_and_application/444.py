


import re

pattern = r'\w'
string = 'Hello abc'

# mach_object = re.match(pattern, string)
# print(mach_object.group())

# string = 'abc, awA.,c, abbbc, aSc'
all_i = re.findall(pattern, string)
print(all_i)
print(bool(all_i))

# fix_t = re.sub(pattern, 'abc', string)
# print(fix_t)



