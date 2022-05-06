num = int(input('Digite um número inteiro entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade(s): {}'.format(u))
print('Dezena(s): {}'.format(d))
print('Centena(s): {}'.format(c))
print('Milhar(es): {}'.format(m))
#num = input('Digite um número inteiro de 0 a 9999: ')
#tamanho = len(num)
#print('Unidade: {}'.format(num[tamanho-1]))
#if tamanho > 1:
#    print('Dezena: {}'.format(num[tamanho-2]))
#if tamanho > 2:
#    print('Centena: {}'.format(num[tamanho-3]))
#if tamanho > 3:
#    print('Milhar: {}'.format(num[tamanho-4]))
