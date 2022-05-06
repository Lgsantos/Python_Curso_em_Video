listagem = ('Produto 1', 345.45, 'Produto 2', 2.90, 'Produto 3', 4.20)
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
# for p in listagem:
#     if (listagem.index(p)+1)%2 != 0:
#         produto = p
#         print(f'{produto:.<24}R$',end='')
#     else:
#         preço = p
#         print(f'{preço:>8.2f} reais')
for pos in range(0, len(listagem)):
    if pos%2 == 0:
        print(f'{listagem[pos]:.<24}R$',end='')
    else:
        print(f'{listagem[pos]:>8.2f} reais')
print('-'*40)