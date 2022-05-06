print('-'*19)
#print('     BANCO CEV     ')
print(f'{"BANCO CEV":^19}')
print('-'*19)
notas_50 = notas_20 = notas_10 = notas_1 = 0
while True:
    valor = int(input('Qual valor você quer sacar? R$'))
    notas_50 = valor // 50
    notas_20 = (valor%50) // 20
    notas_10 = ((valor%50)%20) // 10
    notas_1  = ((valor%50)%20)%10
    if notas_50 != 0: print(f'Total de {notas_50} cédula(s) de R$50.00')
    if notas_20 != 0: print(f'Total de {notas_20} cédula(s) de R$20.00')
    if notas_10 != 0: print(f'Total de {notas_10} cédula(s) de R$10.00')
    if notas_1 != 0: print(f'Total de {notas_1} cédula(s) de R$1.00')
    print('='*19)
    cont = input('Deseja fazer mais um saque? [S/N] ').strip().upper()
    while cont not in 'SN':
        cont = input('Deseja fazer mais um saque? [S/N] ').strip().upper()
    if cont == 'N': break
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')