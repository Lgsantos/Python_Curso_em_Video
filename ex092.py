from datetime import date
#from datetime import datetime
trabalhador = {}
trabalhador['nome'] = input('Nome: ')
idade = date.today().year - int(input('Ano de Nascimento: '))
#idade = datetime.now().year - int(input('Ano de Nascimento: '))
trabalhador['idade'] = idade
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano da Contratação: '))
    trabalhador['salário'] = int(input('Salário: '))
    trabalhador['aposentadoria'] = idade + (35 - (date.today().year - trabalhador['contratação']))
print('-=' * 40)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')


