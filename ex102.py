def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número, dando opção de mostrar cálculo na tela antes de retornar
    o resultado.
    :param num: Número para o qual será calculado o fatorial.
    :param show: Opcional - True: mostra cálculo na tela; False: não mostra cálculo na tela
    :return: retorna um número inteiro igual ao fatorial de "num"
    Função criada por Luís Gustavo dos Santos em 27/06/2020
    """
    from time import sleep
    f = 1
    for v in range(num, 1, -1):
        f *= v
        if show:
            print(f'{v}', end='x')
            sleep(0.3)
    if show: print(f'1 = {f}')
    return f


n = int(input('Digite um número: '))
while True:
    m = input('Gostaria de ver o cálculo? [S/N] ').upper().strip()[0]
    if m in 'SN': break
    print('Valor inválido! Tente novamente...')
if m == 'S':
    m = True
else:
    m = False
print(f'O fatorial de {n} é igual a {fatorial(n, m)}')

#help(fatorial)