# --------------------------------------------------
# Programm by Yoatn
#
# Start date   02.11.2017   23:00
# End date     00.00.2017   00:00
#  
# Description:
#
# --------------------------------------------------

def create(lst, ns, parent):# Готово и работает
    if parent not in lst:
        lst.setdefault(parent, [ns])
    else:
        lst[parent].append(ns)
    return lst

def add(lst, ns, var):
    lst[ns].append(var)
    return lst

def get(lst1, lst2, ns, var): #nss, variables, ns, var
    if var in lst2[ns]:
        return var

# nss = {'global': None}
# variables = {}
nss = {'global': []}
variables = {'global': []}

for i in range(int(input())):
    cmd, ns, var = input().split() #create <namespace> <parent>
    if cmd == 'create':
        create(nss, ns, var)
        if ns is not variables:
            variables[ns] = []
        # print('namespaces', nss)
        # print('variables', variables)
    if cmd == 'add':
        add(variables, ns, var)
        # print('namespaces', nss)
        # print('variables', variables)
    if cmd == 'get':
        print(get(nss, variables, ns, var))

print('namespaces', nss)
print('variables', variables)


