def aumentar(num, per, moe=False):
    num *= (1 + per / 100)
    if moe:
        return moeda(num)
    else:
        return num


def diminuir(num, per, moe=False):
    num *= (1 - per / 100)
    if moe:
        return moeda(num)
    else:
        return num


def dobro(num, moe=False):
    if moe:
        return moeda(num * 2)
    else:
        return num * 2


def metade(num, moe=False):
    if moe:
        return moeda(num / 2)
    else:
        return num / 2


def moeda(num):
    return f'R${num:.2f}'.replace('.',',')


def resumo(num, aum, red):
    print(f'-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    #print(f'{"RESUMO DO VALOR"}'.center(30))
    print(f'-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(num):<10}')
    #print(f'{"Preço analisado:"}\t{moeda(num):<10}') #\t - tabulação
    print(f'{"Dobro do preço:":<20}{dobro(num, True):<10}')
    print(f'{"Metade do preço:":<20}{metade(num, True):<10}')
    print(f'{aum:<2}%{" de aumento:":<17}{aumentar(num, aum, True)}')
    print(f'{red:<2}%{" de redução:":<17}{diminuir(num, red, True)}')