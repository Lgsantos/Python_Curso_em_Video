#CONDICIONAIS - IF - ELSE
#Apenas com IF: condição simples
#Com IF e ELSE: condição composta
#IF e ELSE na mesma linha: condição simplificada

nome = input('Qual é seu nome? ')
if nome == 'Gustavo':
    print('Bom dia, {}\nQue nome lindo!'.format(nome))
else:
    print('Bom dia {}'.format(nome))

print('Parabéns!' if nome == 'Gustavo' else 'Até mais!')
