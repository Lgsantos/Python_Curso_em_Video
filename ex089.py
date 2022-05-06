boletim = []; aluno = []; notas = []
sair = False; num = 0
while True:
    aluno.append(num)
    aluno.append(input('Nome: ').capitalize().strip())
    for i in range(0,2):
        notas.append(float(input(f'Nota {i+1}: ')))
    aluno.append(notas[:])
    aluno.append((notas[0]+notas[1])/2)
    boletim.append(aluno[:])
    aluno.clear()
    notas.clear()
    num += 1
    while True:
        cont = input('Quer continuar? [S/N]').upper().strip()[0]
        if cont == 'N':
            sair = True
            break
        elif cont == 'S': break
        print('Opção inválida!')
    if sair: break
print('-='*10)
print(f'{"No.":<3} {"NOME":<9}  {"MÉDIA":<5}')
print('-'*20)
for a in boletim:
    print(f'{a[0]:>3} {a[1]:<9} {a[3]:>5.1f}')
print('-'*20)
sair = False
while True:
    while True:
        n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        if n == 999:
            sair = True
            break
        elif not 0 <= n < num: print('Opção inválida!')
        else:
            print(f'As notas de {boletim[n][1]} são {boletim[n][2]}')
            print('-' * 20)
    if sair: break
print(f'{"ATÉ LOGO!":-^20}')