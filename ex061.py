termo1 = float(input('Qual o primeiro termo da PA? '))
razão = float(input('Qual a razão da PA? '))
c = 0
while c < 10:
    print('{:.2f}'.format(termo1+c*razão), end=' -> ')
    c += 1
print('ACABOU')

