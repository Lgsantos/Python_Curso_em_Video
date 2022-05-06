lista = [[], []]
for i in range(1,8):
    v = int(input(f'Digite o {i}º valor: '))
    lista[0].append(v) if v%2==0 else lista[1].append(v)
print('-='*25)
print(f'Os valores pares digitados foram {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram {sorted(lista[1])}')
