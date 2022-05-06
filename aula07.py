#n = input('Qual é o seu nome? ')
n = 'Gustavo'
print('Prazer em te conhecer, {:20}!'.format(n))
print('Prazer em te conhecer, {:<20}!'.format(n))
print('Prazer em te conhecer, {:>20}!'.format(n))
print('Prazer em te conhecer, {:^20}!'.format(n))
print('Prazer em te conhecer, {:=^20}!'.format(n))
print('Prazer em te conhecer, {:$<20}!'.format(n))
print('Prazer em te conhecer, {:&>20}!'.format(n))

n1 = 3
n2 = 2
s = n1 + n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a divisão é {:.2f}, a divisão inteira é {}'.format(s, d, di))
print('A multiplicação é {} e a potência é {}'.format(m, e))

print('A soma é {}, a divisão é {:.2f}, a divisão inteira é {}'.format(s, d, di), end=' ')
print('A multiplicação é {} e a potência é {}'.format(m, e))

print('A soma é {}, a divisão é {:.2f}, a divisão inteira é {}'.format(s, d, di), end='>>>')
print('A multiplicação é {} e a potência é {}'.format(m, e))

print('A soma é {}, \n a divisão é {:.2f}, \n a divisão inteira é {}'.format(s, d, di))
print('A multiplicação é {} e a potência é {}'.format(m, e))