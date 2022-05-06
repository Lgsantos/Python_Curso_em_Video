opt = 4
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
while opt != 5:
    opt = int(input('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR
OPÇÃO: '''))
    if opt == 1:
        print('A soma de {} e {} é {}'.format(n1,n2,n1+n2))
    elif opt == 2:
        print('A multiplicação de {} e {} é {}'.format(n1,n2,n1*n2))
    elif opt == 3:
        if n1>n2:
            print('O maior número entre {} e {} é {}'.format(n1,n2,n1))
        elif n1<n2:
            print('O maior número entre {} e {} é {}'.format(n1,n2,n2))
        else:
            print('{} e {} são iguais'.format(n1, n2))
    elif opt == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
print('FIM')
