from random import randint

print('=-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-='*20)
cont = 0
while True:
    n = int(input('Digite um número: '))
    opt = input('Par ou Ímpar? [P/I]: ').strip().upper()
    while opt not in 'PI':
        opt = input('Par ou Ímpar? [P/I]: ').strip().upper()
    cpu = randint(0,9)
    if ((n+cpu)%2 != 0 and opt == 'P') or ((n+cpu)%2 == 0 and opt == 'I'): break
    cont += 1
    PI = 'PAR' if opt=='P' else 'ÍMPAR'
    print(f'Você escolheu {n} e o computador {cpu}. {n + cpu} é {PI}')
    print(f'Você ganhou! Vamos jogar novamente...')
    print(f'=-=' * 20)
if opt == 'P':
    print(f'Você escolheu {n} e o computador {cpu}. {n+cpu} é ÍMPAR.')
    print(f'Perdeu! Você ganhou {cont} vez(es)')
if opt == 'I':
    print(f'Você escolheu {n} e o computador {cpu}. {n+cpu} é PAR.')
    print(f'Perdeu! Você ganhou {cont} vez(es)')


