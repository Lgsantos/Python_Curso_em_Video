lista = []
sair = False
n = 0
while True:
    v = int(input('Digite um valor: '))
    n += 1
    if v not in lista: lista.append(v)
    while True:
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if continuar == 'N':
            sair = True
            break
        elif continuar == 'S': break
    if sair: break
print('-='*30)
print(f'Você digitou {n} elementos')
print(f'Os valores em ordem decrescentes são {sorted(lista,reverse=True)}')
# lista.sort(reverse=True)
# print(f'Os valores em ordem decrescentes são {lista}')
if 5 in lista:
    print(f'O valor 5 está na posição {sorted(lista).index(5)} da lista')
else:
    print('O valor 5 não foi encontrado na lista')
