num = int(input('Digite um número inteiro: '))
base = int(input('Quer convertê-lo para qual base?\n'
                 'Digite 1 para BINÁRIO\n'
                 'Digite 2 para OCTAL\n'
                 'Digite 3 para HEXADECIMAL\n'
                 'Escolha: '))
if base == 1:
    print('Resultado da conversão: {:b}'.format(num))
    print('Resultado da conversão: {}'.format(bin(num)[2:]))
elif base == 2:
    print('Resultado da conversão: {:o}'.format(num))
    print('Resultado da conversão: {}'.format(oct(num)[2:]))
else:
    print('Resultado da conversão: {:x}'.format(num))
    print('Resultado da conversão: {}'.format(hex(num)[2:]))
