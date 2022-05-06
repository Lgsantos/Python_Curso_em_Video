from random import randint
from time import sleep
jogo = []
print('-'*38)
# print('{:^25}'.format("JOGO DA MEGA SENA"))
print(f'{"JOGO DA MEGA SENA":^38}')
print('-'*38)
num = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*4,f' SORTEANDO {num} TESTES ', '-='*4)
for i in range(0,num):
    while len(jogo)<6:
        v = randint(1,60)
        if v not in jogo: jogo.append(v)
    print(f'Jogo {i+1}: {sorted(jogo)}')
    sleep(0.5)
    jogo.clear()
print(f'{" BOA SORTE ":=^38}')