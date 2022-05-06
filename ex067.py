while True:
    n = int(input('Quer a tabuada de qual número? [Número negativo p/ parar]: '))
    if n < 0: break
    c = 1
    while c < 11:
        print(f'{n} x {c:2} = {n*c}')
        c += 1
    print('=' * 15)
print('Programa Tabuada encerrado.')