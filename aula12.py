# Condições aninhadas: if, elif, elif, ... , elif, else

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito, {}!'.format(nome))
elif nome in 'Ana Pedro André Paulo': # pode ser usado sem o else, mas nunca sem o if
    print('{}, seu nome é bem legal!'.format(nome))
else: # pode ser usado sem o elif, mas nunca sem o if
    print('Seu nome é comum, {}.'.format(nome))
print('Tenha um bom dia!')
