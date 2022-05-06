jogador = {}
gols = []
jogador['nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(1,partidas+1):
    gols.append(int(input(f'Quantas gols na {p}ª partida? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i in range(1,len(gols)+1):
    print(f'    -> Na {i}ª partida, fez {gols[i-1]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
