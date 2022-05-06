# VARIÁVEIS COMPOSTAS: DICIONÁRIOS  - estruturas similares às tuplas e lista onde podemos personalizar os
#                                    índices (por exemplo, com strings), ao invés de usar apenas números inteiros
#                                   - são declarados com {} ou dict()
#                                   - Ex. dados = {'nome':'Pedro','idade':25} portanto print(dados['nome'])
#                                   - Para adicionar novos elementos não se usa append. Basta dados['sexo']='M'
#                                   - Para remover elementos: del dados['idade']
#                                   - Dicionários têm VALORES, CHAVES e ITENS
filme = {
    'título': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())
for k,v in filme.items(): # items() é similar ao enumerate() para tuplas e listas
    print(f'O {k} é {v}')

filme2 = {
    'título': 'Matrix',
    'ano': 1999,
    'diretor': 'Wachowski'
}
locadora = []
locadora.append(filme)
locadora.append(filme2)
print(locadora)
print(locadora[0]['ano'])
print(f'O filme {filme["título"]} foi dirigido por {filme["diretor"]}') # tem que usar aspas duplas nas keys

del filme['diretor']
print(filme)

filme['ano'] = 1978
print(filme)
filme['diretor'] = 'George Lucas'
print(filme)

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('unidade da federação: '))
    estado['sigla'] = str(input('sigla: '))
    brasil.append(estado.copy()) # para copiar conteúdo de listas usamos [:] (fatiamento completo), para
                                # dicionários usamos o método copy() - senão é criada uma ligação entre
                                # as estruturas de dados ao invés de só copiar seu conteúdo
print(brasil)