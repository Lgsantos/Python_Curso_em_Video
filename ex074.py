from random import randint

aleatória = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
# maior = sorted(aleatória)[-1]
# menor = sorted(aleatória)[0]
print(f'Os valores sorteados foram: ',end='')
for c in aleatória: print(f'{c}',end=' ')
# print(f'\nO maior valor sorteado foi {maior}')
# print(f'O menor valor sorteado foi {menor}')
# OUTRA FORMA SERIA USAR AS BUILT-IN FUNCTIONS MAX E MIN
print(f'\nO maior valor sorteado foi {max(aleatória)}')
print(f'O menor valor sorteado foi {min(aleatória)}')

