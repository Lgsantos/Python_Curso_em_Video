from random import randint
from time import sleep
from operator import itemgetter
jogadores = {
    'Jogador1': randint(0,6),
    'Jogador2': randint(0,6),
    'Jogador3': randint(0,6),
    'Jogador4': randint(0,6)
}
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
print('Ranking dos jogadores:')
ranking = []
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

# primeiro = (sorted(jogadores.items(), key=lambda item: item[1],reverse=True))[0]
# segundo = (sorted(jogadores.items(), key=lambda item: item[1],reverse=True))[1]
# terceiro = (sorted(jogadores.items(), key=lambda item: item[1],reverse=True))[2]
# quarto = (sorted(jogadores.items(), key=lambda item: item[1],reverse=True))[3]
# print(f'1º lugar: {primeiro[0]} com {primeiro[1]}')
# print(f'2º lugar: {segundo[0]} com {segundo[1]}')
# print(f'3º lugar: {terceiro[0]} com {terceiro[1]}')
# print(f'4º lugar: {quarto[0]} com {quarto[1]}')
