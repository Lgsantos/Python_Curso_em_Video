soma = 0
quantos = 0
for c in range(1,501,2):
    if c%3==0:
        print(c, end=' ')
        soma += c
        quantos += 1
print('\nA soma desses {} números é {}.'.format(quantos, soma))