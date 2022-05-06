n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))
# if n1 > n2:
#     if n1 > n3:
#         print('{} é o maior'.format(n1))
#         print('{} é o menor'.format(n2) if n2 < n3 else\
#                   '{} é o menor'.format(n3))
#     else:
#         print('{} é o maior'.format(n3))
#         print('{} é o menor'.format(n1) if n1 < n2 else \
#                   '{} é o menor'.format(n2))
# else:
#     if n2 > n3:
#         print('{} é o maior'.format(n2))
#         print('{} é o menor'.format(n1) if n1 < n3 else\
#                   '{} é o menor'.format(n3))
#     else:
#         print('{} é o maior'.format(n3))
#         print('{} é o menor'.format(n1) if n1 < n2 else \
#                   '{} é o menor'.format(n2))

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('{} é o menor valor'.format(menor))
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('{} é o maior valor'.format(maior))