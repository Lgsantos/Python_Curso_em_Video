from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = int(date.today().year)-ano
if idade <= 9:
    print('A categoria do atleta é MIRIM.')
elif idade <= 14:
    print('A categoria do atleta é INFANTIL')
elif idade <= 19:
    print('A categoria do atleta é JUNIOR.')
elif idade <= 20:
    print('A categoria do atleta é SÊNIOR.')
else:
    print('A categoria do atleta é MASTER')
