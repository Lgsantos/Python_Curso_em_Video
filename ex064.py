c = soma = cont = 0
c = int(input('Digite um número: [999 p/ parar] '))
while c != 999:
    soma += c
    cont += 1
    c = int(input('Digite um número: [999 p/ parar] '))
print('A soma dos {} números digitados é {}.'.format(cont, soma))