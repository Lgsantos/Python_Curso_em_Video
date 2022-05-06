lista = []
lista_pares = []
lista_ímpares = []
sair = False
while True:
    n = int(input('Digite um valor: '))
    if n not in lista: lista.append(n)
    while True:
        cont = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if cont == 'N':
            sair = True
            break
        elif cont == 'S': break
    if sair: break
for i in lista:
    lista_pares.append(i) if i%2==0 else lista_ímpares.append(i)
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_ímpares}')