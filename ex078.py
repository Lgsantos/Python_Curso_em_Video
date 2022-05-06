lista = []
for i in range(0,5):
    lista.append(int(input(f'Digite um número para a posição {i}: ')))
print('-='*15)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for p, l in enumerate(lista):
    if l == max(lista): print(f'{p}... ',end='')
print()
print(f'O menor valor digitado foi {min(lista)} nas posições ', end='')
for p, l in enumerate(lista):
    if l == min(lista): print(f'{p}... ',end='')