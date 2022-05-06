from random import randint
r = randint(2,5)
c = maior = menor = soma = 0
while c < r:
    n = int(input('Digite um número inteiro: '))
    if c == 0:
        maior = menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma += n
    c += 1
    if c == r:
        print('''
A média dos números digitados é {:.2f}.
O maior número foi {}.
O menor número foi {}.
'''.format(soma/c,maior,menor))
        continuar = input('Deseja continuar? [S/N] ').upper().strip()
        if continuar == 'S':
            r += randint(2,5)
        else:
            print('FIM')

