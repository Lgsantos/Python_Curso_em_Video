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


def menu(lst):
    from uteis import números
    for item, value in enumerate(lst):
        print(f'\033[0;32m {item+1} - \033[m\033[0;36m{value}\033[m')
    print('~' * 42)
    opc = números.leiaint('\033[0;32mSua opção: \033[m')
    return opc