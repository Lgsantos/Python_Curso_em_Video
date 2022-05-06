from random import randrange

n = randrange(0,5)
num = int(input('Adivinhe o número secreto inteiro de 0 a 5: '))
print('Você acertou!' if num == n else 'Você errou!')