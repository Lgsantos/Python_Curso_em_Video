def escreve(msg):
    print('-=' * 40)
    print(msg)


def contagem(i, f, p):
    from time import sleep
    if i <= f:
        if p == 0: p = 1
        if p < 0: p = -p
        escreve(f'Contagem de {i} até {f}, de {p} em {p}')
        for j in range(i, f+1, p):
            print(j, end=' ')
            sleep(0.25)
    elif i > f:
        if p == 0: p = -1
        if p < 0: p = -p
        escreve(f'Contagem de {i} até {f}, de {p} em {p}')
        for j in range(i, f-1, -p):
            print(j, end=' ')
            sleep(0.25)
    print('FIM!')
    sleep(0.5)


contagem(1, 10, 1)
contagem(10, 0, 2)
escreve('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contagem(ini, fim, pas)