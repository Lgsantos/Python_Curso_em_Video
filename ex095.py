jogador = {}; gols = []; grupo = []; cont = 'x'
while True:
    print('-'*30)
    jogador['nome'] = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1,partidas+1):
        gols.append(int(input(f'Quantas gols na {p}ª partida? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    while cont not in 'SN':
        cont = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if cont == 'N':
        sair = True
        grupo.append(jogador.copy())
        jogador.clear()
        gols.clear()
        break
    grupo.append(jogador.copy())
    jogador.clear()
    gols.clear()
    cont = 'x'
print('-=' * 30)
print(f'cod  nome        gols        total')
print('-' * 60)
for i, j in enumerate(grupo):
    print(f'{i + 1:>2} {j["nome"]:<11} {str(j["gols"]):<14} {j["total"]:<2}')
print('-' * 60)
while True:
    j = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    while j not in range(1,len(grupo)+1) and j != 999:
        print(f'ERRO! Não existe jogador com o código {j}! Tente novamente...')
        j = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if j == 999: break
    print(f'-- LEVANTAMENTO DO JOGADOR {grupo[j-1]["nome"]}:')
    for i in range(1, len(grupo[j-1]['gols'])+1):
        print(f'   No jogo {i} fez {grupo[j-1]["gols"][i-1]} gols.')
    print('-' * 60)
print('VOLTE SEMPRE!')
