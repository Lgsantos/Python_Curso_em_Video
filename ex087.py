matriz = []; elemento = []; l =  soma_pares = soma_col3 = 0
for l in range(0,3):
    for c in range(0,3):
        elemento.append(l)
        elemento.append(c)
        elemento.append(int(input(f'Digite um valor para [{l},{c}]: ')))
        matriz.append(elemento[:])
        elemento.clear()
print('-='*25)
for l in range(0,9):
    if l < 3: print(f'[ {matriz[l][2]} ]', end='')
    if l == 3: print()
    if 3 <= l < 6: print(f'[ {matriz[l][2]} ]', end='')
    if l == 6: print()
    if 6 <= l < 9: print(f'[ {matriz[l][2]} ]', end='')
print()
print('-='*25)
for l in range(0,9):
    if matriz[l][2]%2 == 0: soma_pares += matriz[l][2]
    if l == 2 or l == 5 or l == 8: soma_col3 += matriz[l][2]
    if l == 3: maior_lin2 = matriz[l][2]
    if 4 <= l <= 5 and matriz[l][2] > maior_lin2: maior_lin2 = matriz[l][2]
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da 3ª coluna é {soma_col3}')
print(f'O maior valor da 2ª linha é {maior_lin2}')
