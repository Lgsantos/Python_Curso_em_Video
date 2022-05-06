def título(str, b=41):
    """
    -> Cria cabeçalhos coloridos que acompanham a largura da string.
    :param str: String do título do cabeçalho
    :param b: código da cor de fundo: 41-Vermelho, 42-Amarelo...
    :return: Não há retorno.
    Função criada por Luís Santos em 28/06/2020
    """
    print(f'\033[30:{b}m~\033[m' * (len(str) + 4))
    print(f'\033[1:30:{b}m  {str}  \033[m')
    print(f'\033[30:{b}m~\033[m' * (len(str) + 4))


def ajuda():
    """
    -> Busca informações sobre comando Python e mostra na tela.
    :return: Não há retorno.
    Função criada por Luís Santos em 28/06/2020
    """
    from time import sleep
    while True:
        título('SISTEMA DE AJUDA PyHELP')
        func = input('Digite um Função ou Biblioteca: ("end" para sair) ').strip().lower()
        if func == 'end': break
        título(f'Acessando o manual do comando "{func}"', 43)
        sleep(0.5)
        print(f'\033[1:30:44m', end='')
        help(func)
        print(f'\033[m')
        sleep(0.5)
    título('ATÉ LOGO')


ajuda()