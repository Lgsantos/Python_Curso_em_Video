def notas(* n, s=False):
    """
    -> Recebe notas dos alunos de uma classe, calcula estatísticas e mostra como um dicionário.
    :param n: um ou mais notas dos alunos, separados por vírgula.
    :param s: Opcional. Se s=True, função mostra situação da classe; Se s=False ou omitido, não
            mostra situação da classe.
    :return: Um dicionário com as informações calculadas
    """
    estat = {}
    estat['Total'] = len(n)
    estat['Maior'] = max(n)
    estat['Menor'] = min(n)
    estat['Média'] = sum(n) / len(n)
    if s:
        if estat['Média'] >= 7:
            sit = 'BOA'
        elif 5<= estat['Média'] < 7:
            sit = 'REGULAR'
        else:
            sit = 'RUIM'
        estat['Situação'] = sit
    #print(f'{estat}')
    return estat


resposta = notas(1, 3, 10, s=True)
# help(notas)
print(resposta)