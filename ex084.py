pessoas = []; dado = []; pesos = []; cont = 0; sair = False
while True:
    dado.append(input('Digite o nome: '))
    dado.append(float(input('Digite o peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    cont += 1
    while True:
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if continuar == 'N':
            sair = True
            break
        if continuar == 'S': break
    if sair: break
for p in pessoas:
    pesos.append(p[1])
maior_peso = max(pesos)
menor_peso = min(pesos)
print('-='*25)
print(f'Ao todo, você cadastrou {cont} pessoas')
print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1]==maior_peso: print(f'{p[0]}...', end='')
print(f'\nO menor peso foi de {menor_peso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1]==menor_peso: print(f'{p[0]}...', end='')

