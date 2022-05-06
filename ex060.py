num = int(input('Digite um número inteiro: '))
c = num
f = 1
print('{}! = '.format(c), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))


# from math import factorial
# num = int(input('Digite um número inteiro: '))
# print('{}! = {}'.format(num,factorial(num)))

# num = int(input('Digite um número inteiro: '))
# fator = 1
# fatorial = num
# while num-fator > 1:
#     fatorial = fatorial*(num-fator)
#     fator += 1
# print('{}! = {}.'.format(num,fatorial))
