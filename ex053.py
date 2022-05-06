frase = input('Digite uma frase: ').strip()
frase_sem_espaços = frase.replace(' ','').upper()
inverso = ''
# l = len(frase_sem_espaços)
# for c in range(l-1,-1,-1):
#     inverso += frase_sem_espaços[c]
inverso = frase_sem_espaços[::-1] # O PYTHON É F#D@!!!!!!!
if frase_sem_espaços==inverso:
    print('A frase "{}" é um palíndromo.'.format(frase))
else:
    print('A frase "{}" não é um palíndromo.'.format(frase))
