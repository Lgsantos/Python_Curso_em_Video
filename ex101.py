def voto(ano):
    """
    -> Recebe o ano de nascimento de uma pessoa e diz qual sua condição de eleitor.
    :param ano: Ano de nascimento da pessoa.
    :return: Sem retorno de valores.
    Função criada por Luís Santos em 28/06/2020
    """
    from datetime import datetime # importando localmente salva memória de processamento, pois só é utilizada enquanto a
                                    # rotina estiver sendo executada.
    idade = datetime.now().year - ano
    if idade < 16:
        print(f'Com {idade} o voto é NEGADO')
    elif 18 <= idade <= 65:
        print(f'Com {idade} o voto é OBRIGATÓRIO')
    else:
        print(f'Com {idade} o voto é OPCIONAL')


voto(int(input('Em que ano você nasceu? ')))
