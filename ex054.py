from datetime import date

maiores = 0
menores = 0
ano_atual = date.today().year
for c in range(0,7):
    ano = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(c+1)))
    if ano_atual - ano >= 18:
        maiores += 1
    else:
        menores += 1
print('''
{} dessas pessoas ainda não atingiram a maioridade.
{} já são maiores.'''.format(menores,maiores))