n = int(input('Digite um número inteiro: '))
a = c = 0
b = f = 1
print('0 -> 1 -> ', end='')
while c < n-2:
    f = a + b
    print('{}'.format(f), end=' -> ')
    a = b
    b = f
    c += 1
print('FIM')