def leiaint(s):
    """
    -> Similar à função INPUT(), mas validando se entrada é número e com tratamento de exceções.
    :param s: Pergunta a ser apresentada para o usuário, solicitando um número.
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
            return f'{n}'


def leiafloat(str):
    import atexit
    while True:
        n = input(str)
        try:
            n = float(n)
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[0;31mERRO: Usuário interrompeu a entrada de dados.\033[m')
        else:
            return f'{n}'



def adeus():
    print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
    n = 0
    return n


num = leiaint('Digite um número inteiro: ')
num2 = leiafloat('Digite um número real: ')
print(f'O número inteiro foi {num} e o real foi {num2}')