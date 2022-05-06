salario = float(input('Digite o salário do funcionário: '))
print('Aumento será {} reais'.format(salario*10/100) if salario > 1250.0\
      else 'Aumento será {} reais'.format(salario*15/100))