# for c in range(0,3):
#     print('Oi')
# print('FIM')
#
# for c in range(6,0,-1):
#     print(c)
# print('FIM')
#
# for c in range(0,7,2):
#     print(c)
# print('FIM')
# n = int(input('Digite um número inteiro: '))
# for c in range(0,n+1):
#     print(c)
# print('FIM')
# i = int(input('Digite o início: '))
# f = int(input('Digite o fim: '))
# p = int(input('Digite o passo: '))
# for c in range(i,f+1,p):
#     print(c)
# print('FIM')
s = 0
for c in range(0,3):
    n = int(input('Digite um número: '))
    s += n # equivalente de s = s + n
print('O somatório de seus números é {}.'.format(s))
