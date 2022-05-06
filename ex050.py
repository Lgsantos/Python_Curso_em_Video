s = 0
for c in range(0,6):
    n = int(input('Digite o {}° número: '.format(c+1)))
    if n%2==0: s += n
print('A soma dos números pares que você digitou é {}'.format(s))
