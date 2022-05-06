maiores = homens = mulheres_menos_20 = 0
while True:
    print('=-' * 13)
    print('   CADASTRE UMA PESSOA   ')
    print('=-' * 13)
    idade = int(input('Idade: '))
    if idade > 18: maiores += 1
    sexo = input('Sexo: [M/F] ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    if sexo == 'M': homens += 1
    if idade < 20 and sexo == 'F': mulheres_menos_20 += 1
    cont = input('Deseja continuar? [S/N]').strip().upper()[0]
    while cont not in 'SN':
        cont = input('Deseja continuar? [S/N]').strip().upper()[0]
    if cont == 'N': break
#print('=====FIM DO PROGRAMA=====')
print(f'{"FIM DO PROGRAMA":=^25}')
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homem(ns) cadastrado(s)')
print(f'E temos {mulheres_menos_20} mulher(es) com menos de 20 anos')