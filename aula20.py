#   FUNÇÕES - automatizar rotinas (tarefas repetitivas)
#           - Python permite "desempacotar" parâmetros das funções: ou seja, o número de parâmetros pode
#           ser variável (outras linguagens não permitem isso!)
def mostralinha():
    print('-' * 30)


def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


def soma(a, b):
    s = a + b
    print(s)


def contador(* núm): # Os parâmetros são desempacotados em um tupla
    print(f'O tamanho da tupla {núm} é {len(núm)}')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# PROGRAMA PRINCIPAL
mostralinha()
print(f'{"CADASTRO DE ALUNOS":^30}')
mostralinha()

mensagem('CADASTRO DE ALUNOS')

mostralinha()
soma(4, 9)
soma(-3, 4)
soma(a=3, b=4)# passando parâmetros de forma explícita
soma(b=1, a=8)# não precisam estar na ordem correta

mostralinha()
contador(1, 6, 3)
contador(4)
contador(3, 8, 11, 2)

mostralinha()
vetor = [1, 6, 3, 9, 10]
print(vetor)
dobra(vetor)
print(vetor)