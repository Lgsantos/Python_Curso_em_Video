import random
import time

escolha = int(input('Pedra, papel ou tesoura?\n'
                    'Digite 1 para PEDRA\n'
                    'Digite 2 para PAPEL\n'
                    'Digite 3 para TESOURA\n'
                    'Escolha: '))
#opcoes = ['Pedra', 'Papel', 'Tesoura']
#escolha_cpu = random.choice(opcoes)
opcoes = ('Pedra', 'Papel', 'Tesoura')
cpu = random.randint(0,1)
escolha_cpu = opcoes[cpu]
if escolha == 1:
    if escolha_cpu == 'Papel':
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO')
        time.sleep(1)
        print('{} vence Pedra. Você perdeu!'.format(escolha_cpu))
    elif escolha_cpu == 'Tesoura':
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO')
        time.sleep(1)
        print('Pedra vence {}. Você ganhou!'.format(escolha_cpu))
    else:
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO')
        time.sleep(1)
        print('Pedra com {}. Empatamos!'.format(escolha_cpu))
elif escolha == 2:
    if escolha_cpu == 'Papel':
        print('Papel com {}. Empatamos!'.format(escolha_cpu))
    elif escolha_cpu == 'Tesoura':
        print('{} vence Papel. Você perdeu!'.format(escolha_cpu))
    else:
        print('Papel vence {}. Você ganhou!!'.format(escolha_cpu))
else:
    if escolha_cpu == 'Papel':
        print('Tesoura vence {}. Você ganhou!'.format(escolha_cpu))
    elif escolha_cpu == 'Tesoura':
        print('{} com Tesoura. Empatamos!'.format(escolha_cpu))
    else:
        print('{} vence Tesoura. Você perdeu!!'.format(escolha_cpu))