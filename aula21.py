#   FUNÇÕES (PARTE 2) - INTERACTIVE HELP: basta usar função help() no Python Console. Para sair: quit
#                                           Também podemos usar help() em um programa: e.x. help(print)
#                                               ou print(<comando>.__doc__)
#                       DOCSTRINGS: São strings de documentação (como as mostradas pelo help()). Podem
#                                   ser criadas para funções criadas pelo programador!
#                                   Basta abrir aspas duplas 3x logo abaixo de def.
#                       ARGUMENTOS OPCIONAIS: Para parâmetros opicionais de uma função, podemos indicar
#                                               qual valor padrão eles deverão assumir caso não sejam
#                                               inseridos pelo usuário. Usa-se "="
#                       ESCOPO DE VARIÁVEIS: Em programação, escopo é o local onde a variável vai existir,
#                                           funcionar. Pode ser GLOBAL, LOCAL. As variáveis globais são
#                                           aquelas declaradas no corpo do programa principal. As locais são
#                                           as declaradas dentro das funções.
#                                           NOTA 1: se um mesmo nome de variável for declarada no programa
#                                           principal e em uma função, dentro da função será usado os valores
#                                           da variável local! Se a variável global for passada para a função,
#                                           seu valor não é afetado pelo valor da equivalente local.
#                                           NOTA 2: Além do escopo das variáveis também há escopo de chamada
#                                           de biblioteca, chamada de função (quando importamos algo, existe
#                                           a importação local e global
#                       RETORNO DE RESULTADOS: através do comando "return". Qualquer tipo de valor pode ser
#                                               retornado (e.x.: True, False, listas, dicionários, tuplas...)
help(print)
print(len.__doc__)
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador)

def somar(a=0, b=0, c=0): # Nada nos impede de colocar todos os parâmetros como opcionais!!!!!!!
    """
    -> Soma até 3 números e mostra na tela.
    :param a: 1º número a ser somado. Se ausente, vale 0.
    :param b: 2º número a ser somado. Se ausente, vale 0.
    :param c: 3º número a ser somado. Se ausente, vale 0.
    :return: Sem retorno.
    Função criada por LGS em 27/06/2020
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(2, 5, 3)
somar(4, 12)
somar(7)
somar()
somar(b=9,c=13)
somar(c=2, a=1)

def função():
    n1 = 4
    print(f'N1 local vale {n1}')


def função2():
    global n1 # comando "global" liga as variáveis local e global n1. O que acontecer com a local, afetará a global
    n1 = 4
    print(f'N1 dentro da função vale {n1}')


n1 = 2
print(f'N1 global vale {n1}')
função()
função2()
print(f'N1 fora da função vale {n1}')

def somar2(a=0, b=0, c=0):
    """
    -> Soma até 3 números e retorna resultado.
    :param a: 1º número a ser somado. Se ausente, vale 0.
    :param b: 2º número a ser somado. Se ausente, vale 0.
    :param c: 3º número a ser somado. Se ausente, vale 0.
    :return: Sem retorno.
    Função criada por LGS em 27/06/2020
    """
    s = a + b + c
    return s


soma = somar2(2, 5, 8)
print(soma)
print(somar2(6, 9, 1))
somas_múltiplas = somar2(2, 5, 8) + somar2(6, 9, 1) + somar2(9, 7)
print(somas_múltiplas)

def fatorial(num=1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return  f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(8)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')

def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
if par(n):
    print(f'{n} é par.')
else:
    print(f'{n} é ímpar.')