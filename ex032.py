from datetime import date

ano = int(input('Digite um ano com 4 dígitos. Coloque 0 se quiser o ano atual: '))

# if ano % 4 == 0:
#     if ano%100 !=0:
#         print('{} é bissexto'.format(ano))
#     else:
#         print('{} é bissexto'.format(ano) if ano%400==0 else\
#                   '{} não é bissexto'.format(ano))
# else:
#     print('{} não é bissexto'.format(ano))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é bissexto'.format(ano))
else:
    print('{} não é bissexto'.format(ano))
