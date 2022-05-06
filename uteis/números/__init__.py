def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


def leiaint(s):
    """
    -> Similar à função INPUT(), mas validando se entrada é número inteiro e com tratamento de exceções.
    :param s: Pergunta a ser apresentada para o usuário, solicitando um número inteiro.
    :return: Valor do número digitado ou texto indicando que entrada não foi numérica.
    Função feita por Luís Santos em 29/06/2020
    """
    while True:
        n = input(f'{s}')
        try:
            n = int(n)
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[0;31mERRO: Usuário interrompeu a entrada de dados.\033[m')
        else:
            return n