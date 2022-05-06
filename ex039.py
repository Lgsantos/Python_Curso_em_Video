import datetime

ano_nascimento = int(input('Qual o ano do seu nascimento? Responda usando 4 dígitos: '))
ano_atual = int(datetime.date.today().year)
idade = ano_atual - ano_nascimento
if idade < 18:
    print('Você ainda não precisa se alistar. Faltam {} anos.'.format(18-idade))
elif idade == 18:
    print('Você precisa se alistar esse ano!')
else:
    print('Você já passou {} anos do tempo do alistamento.'.format(idade-18))

