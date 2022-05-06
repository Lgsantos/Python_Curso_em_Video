def área(l, c):
    a = l * c
    print(f'A área de um terreno {l}m x {c}m é de {a:.1f}m².')


print(f'{"CONTROLE DE TERRENOS":^30}')
print('-'*30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
área(largura, comprimento)
