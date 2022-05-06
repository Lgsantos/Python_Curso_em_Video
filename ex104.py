def leiaint(s):
    """
    -> Similar à função INPUT(), mas validando se entrada é número.
    :param s: Pergunta a ser apresentada para o usuário, solicitando um número.
    :return: Valor do número digitado ou texto indicando que entrada não foi numérica.
    Função feita por Luís Santos em 28/06/2020
    """
    while True:
        n = input(f'{s}')
        if n.isnumeric():
            n = float(n)
            break
        else:
            print(f'\033[31m{n} não é um número válido!\033[m')
    return f'{n:.2f}'


num = leiaint('Digite um número: ')
print(f'{num}')