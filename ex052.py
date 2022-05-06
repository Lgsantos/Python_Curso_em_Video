n = int(input('Digite um número inteiro: '))
s = 0
for c in range(1,n+1):
    if n%c==0:
        s += c
if s==n+1:
    print('{} é primo.'.format(n))
else:
    print('{} não é primo.'.format(n))