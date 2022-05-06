from random import randrange

n = randrange(0,11)
jogadas = 1
num = int(input('Adivinhe o número secreto inteiro de 0 a 5: '))
while num != n:
    print('Você errou! Tente novamente.')
    num = int(input('Adivinhe o número secreto inteiro de 0 a 5: '))
    jogadas += 1
print('Você acertou! Precisou de {} jogadas para isso.'.format(jogadas))