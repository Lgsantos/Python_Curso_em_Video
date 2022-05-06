matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-='*25)
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^3} ]', end='')
    print()
# matriz = []; elemento = []; l1 = l2 = l3 = 0
# for l in range(0,3):
#     for c in range(0,3):
#         elemento.append(l)
#         elemento.append(c)
#         elemento.append(int(input(f'Digite um valor para [{l},{c}]: ')))
#         matriz.append(elemento[:])
#         elemento.clear()
# print('-='*25)
# for l1 in range(0,9):
#     if l1 < 3: print(f'[ {matriz[l1][2]} ]', end='')
#     if l1 == 3: print()
#     if 3 <= l1 < 6: print(f'[ {matriz[l1][2]} ]', end='')
#     if l1 == 6: print()
#     if 6 <= l1 < 9: print(f'[ {matriz[l1][2]} ]', end='')
# for l1 in range(0,3): # outro modo de contruir a matriz, com menos linhas e laços FOR do que o código abaixo
#     print(f'[ {matriz[l1][2]} ]', end='')
# print()
# for l2 in range(3,6):
#     print(f'[ {matriz[l2][2]} ]', end='')
# print()
# for l3 in range(6,9):
#     print(f'[ {matriz[l3][2]} ]', end='')
