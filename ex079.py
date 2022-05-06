lista = []
sair = False
while True:
    v = int(input('Digite um valor: '))
    if v not in lista:
        lista.append(v)
        print('Valor adicionado com sucesso...')
        while True:
            cont = input('Quer continuar? [S/N] ').upper().strip()[0]
            if  cont == 'N':
                sair = True
                break
            elif cont == 'S': break
            print('Opção inválida! Tente novamente...')
        if sair: break
    else: print('Valor duplicado! Não vou adicionar...')
print('-='*30)
print(f'Você digitou os valores {sorted(lista)}')