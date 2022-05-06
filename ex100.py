def sorteia(lst):
    from random import randint
    from time import sleep
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(0,5):
        n = randint(0,100)
        lst.append(n)
        print(f'{n}', end=' ')
        sleep(0.25)
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    for v in lst:
        if v%2 == 0:
            soma += v
    print(f'Somando os valores pares de {lst}, temos {soma}')


números = []
sorteia(números)
somaPar(números)
