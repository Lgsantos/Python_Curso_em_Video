pessoa = {}
grupo = []
while True:
    pessoa['nome'] = input('Nome: ').strip()
    pessoa['sexo'] = input('Sexo: [M/F] ').upper().strip()[0]
    while pessoa['sexo'] not in 'MF':
        print('Opção inválida!')
        pessoa['sexo'] = input('Sexo: [M/F] ').upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    pessoa.clear()
    cont = input('Deseja continuar? [S/N] ').upper().strip()[0]
    while cont not in 'SN':
        print('Opção inválida!')
        cont = input('Deseja continuar? [S/N]').upper().strip()[0]
    if cont == 'N': break
print('-='*30)
print(f'- O grupo tem {len(grupo)} pessoas.')
soma = 0
for i in grupo: soma += i['idade']
média = soma / len(grupo)
print(f'- A média de idade do grupo é {média:.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for i in grupo:
    if i['sexo'] == 'F': print(f'{i["nome"]}', end=' ')
print()
print('A lista de pessoas que estão acima da média:')
print()
for i in grupo:
    if i['idade'] > média:
        for k, v in i.items():
            print(f'{k} = {v}', end='; ')
        print()



