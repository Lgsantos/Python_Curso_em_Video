s = 0
maior_idade = 0
menores_de_20 = 0
mais_velho = 'Ninguém'
for c in range(0,4):
    nome = input('\nQual o nome da {}º pessoa? '.format(c+1))
    idade = int(input('Qual a idade da {}º pessoa? '.format(c+1)))
    sexo = int(input('''Qual o sexo da {}º pessoa?
[ 1 ] HOMEM
[ 2 ] MULHER
Opção: '''.format(c+1)))
    s += idade
    if sexo == 1:
        if idade > maior_idade:
            maior_idade = idade
            mais_velho = nome
    if sexo == 2:
        if idade < 20:
           menores_de_20 += 1
print('''
A média de idade dessas pessoas é de {} anos.
O homem mais velho chama-se {}.
Há {} mulheres com menos de 20 anos.
'''.format(s/4, mais_velho, menores_de_20))
