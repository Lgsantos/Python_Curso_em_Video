print('-'*29)
print('     LOJAS SUPER BARATÃO     ')
print('-'*29)
soma = mais_de_mil = menor_preço = c = 0
while True:
    produto = input('Nome do produto: ')
    preço = float(input('Preço: R$'))
    cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while cont not in 'SN':
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
    soma += preço
    if preço > 1000: mais_de_mil += 1
    if c == 0 or preço < menor_preço:
        menor_preço = preço
        produto_mais_barato = produto
    c += 1
    if cont == 'N': break
#print('-------FIM DO PROGRAMA-------')
print(f'{"FIM DO PROGRAMA":-^30}')
print(f'O total comprado foi de R${soma:.2f}')
print(f'Temos {mais_de_mil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi a/o {produto_mais_barato} que custa R${menor_preço:.2f}')
