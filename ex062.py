termo1 = float(input('Qual o primeiro termo da PA? '))
razão = float(input('Qual a razão da PA? '))
c = 0
f = 10
while c < f:
    print('{:.2f}'.format(termo1+c*razão), end=' -> ')
    c += 1
    if c == f:
        f += int(input('Devo calcular mais quantos termos? '))
print('ACABOU')

