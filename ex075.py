# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# n3 = int(input('Digita mais um número: '))
# n4 =
# tupla = (n1,n2,n3,n4)
#
# O CÓDIGO ACIMA PODE SER SUBSTITUÍDO POR:
tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digita mais um número: ')),
         int(input('Digite o último número: ')))
print(f'Você digitou ou valores: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
#if tupla.count(3)>0:
if 3 in tupla:
    print(f'O valor 3 apareceu primeiro na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for c in tupla:
    if c%2==0: print(c,end=' ')
