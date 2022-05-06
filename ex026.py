frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} nessa frase'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição: {}'.format(frase.find('A')+1))
print('A letra "A" aparece pela última vez na posição: {}'.format(frase.rfind('A')+1))

# frase = input('Digite uma frase: ')
# i = frase.count('a')
# print('A letra "a" aparece {} nessa frase.'.format(i))
# print('A letra "a" aparece primeiramente na posição {}.'.format(frase.find('a')))
# dividida = frase.split('a')
# j = len(dividida)
# ultima = dividida[j-1]
# if ultima == '':
#     print('A letra "a" aparece pela última vez na posição {}.'.format(len(frase)-1))
# else:
#     u = frase.find(ultima) - 1
#     print('A letra "a" aparece pela última vez na posição {}.'.format(u))
