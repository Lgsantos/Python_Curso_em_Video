lista = []
for i in range(0,5):
    v = int(input('Digite um valor: '))
    if i==0 or v>lista[-1]:
        lista.append(v)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
    # OLHA O CÓDIGO ESTÚPIDO QUE FIZ ANTES!!!!!!
    # if len(lista)==0:
    #     lista.append(v)
    #     print(f'Adicionado ao final da lista...')
    # else:
    #     if v < min(lista):
    #         lista.insert(lista.index(min(lista)),v)
    #         print(f'Adicionado na posição {lista.index(min(lista))} da lista...')
    #     elif v > max(lista):
    #         lista.append(v)
    #         print(f'Adicionado ao final da lista...')
    #     else:
    #         if len(lista)==2:
    #             lista.insert(1,v)
    #             print('Adicionado na posição 1 da lista...')
    #         elif len(lista)==3:
    #             if v < lista[1]:
    #                 lista.insert(1, v)
    #                 print(f'Adicionado na posição 1 da lista...')
    #             elif v > lista[1]:
    #                 lista.insert(2, v)
    #                 print(f'Adicionado na posição 2 da lista...')
    #         elif len(lista)==4:
    #             if v < lista[1]:
    #                 lista.insert(1, v)
    #                 print(f'Adicionado na posição 1 da lista...')
    #             elif v > lista[2]:
    #                 lista.insert(3, v)
    #                 print(f'Adicionado na posição 3 da lista...')
    #             else:
    #                 lista.insert(2,v)
    #                 print(f'Adicionado na posição 2 da lista...')
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')