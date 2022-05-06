#   TUPLAS (1º TIPO DE VARIÁVEL COMPOSTA): PARACE UMA LISTA, MAS NÃO É
#           OS OUTROS DOIS TIPOS DE VARIÁVEIS COMPOSTAS SÃO: LISTAS E DICIONÁRIOS
#           Usamos () para tuplas, [] para listas e {} para dicionários.
#           Desde Python 3.5 tuplas podem ser definidas sem ()
#           ATÉ O EX071, TODAS AS VARIÁVEIS UTILIZADAS ERAM SIMPLES. ALGUNS DELES PODERIAM SER OTIMIZADOS USANDO TUPLAS
#           ===============TUPLAS SÃO IMUTÁVEIS===================
#           OBS. UMA STRING É UMA LISTA.
lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
almoço = 'arroz', 'feijão', 'carne de soja', 'batatas'
print(lanche)
print(almoço)
print(almoço[1])
print(lanche[-2]) #Usando valores negativos, fazemos a contagem do último para o primeiro
print(almoço[1:3]) #No 'fatiamento', o último elemento é ignorado
print(lanche[2:])
print(almoço[:2])
print(lanche[-2:])
print(almoço[:-3])
#lanche[1] = 'refrigerante' # Como tuplas são imutáveis, essa linha causa um erro pois a posição 1 já está ocupada por 'suco'
#print(lanche[1])
for comida in lanche:
    print(f'Eu vou comer {comida}')
print(len(almoço))
for c in range(0,len(almoço)):
    print(f'Eu comerei {almoço[c]}')
for c in range(0,len(lanche)):
    print(f'Comi {lanche[c]} na posição {c}')
for pos, comida in enumerate(lanche):
    print(f'Comi {comida} na posição {pos}')
print(sorted(lanche)) #Imprime o conteúdo da tupla lanche de forma ordenada (transformou a tupla em lista - note os parênteses -...
print(lanche) #... mas como tuplas são IMUTÁVEIS, aqui a impressão mostra que a tupla não foi alterada

a = (2,5,3)
b = (8,7,0,3,2)
c = a + b
print(c)
d = b + a
print(d)
print(c.count(7)) #Conta quantas vezes o número 7 apareceu na tupla c
print(c.count(9))
print(d.index(0)) #Retorna a posição do número 8 na tupla
print(d.index(3)) #Retorna a posição da primeira ocorrência de 3
print(d.index(3,4)) #Retorna a posição da primeira ocorrência de 3 a partir da posição 4. Chamamos isso de "deslocamento"

pessoa = ('Gustavo', 43, 'M', 69.8) #No Python não há problema de se misturar tipos diferentes de dados dentro da tupla.
#No Java, as tuplas são mais próximas de vetores, que exigem um único tipo de dado
print(pessoa)
del(pessoa) #Essa linha apaga a tupla, fazendo com que a linha de baixo cause um erro
print(pessoa)