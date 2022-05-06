def ficha(n='<não informado>', g=0):
    """
    -> Mostra a ficha de um jogador na tela.
    :param n: Opcional. Nome do jogador. Se não informado, usa uma string padrão
    :param g: Opcional. Número de gols feitos pelo jogador no campeonato.
    :return: Sem retorno
    Função criada por Luís Santos em 28/06/2020
    """
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
if gols.isnumeric():
    if nome.strip() != '':
        ficha(nome, int(gols))
    else:
        ficha(g = int(gols))
else:
    if nome.strip() != '':
        ficha(nome)
    else:
        ficha()
