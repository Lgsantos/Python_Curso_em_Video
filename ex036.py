print('=$'*20)
print('\033[1:33:44mEMPRÉSTIMO BANCÁRIO\033[m')
print('=$'*20)
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quanto anos quer pagar a casa? '))
prestacao = casa / (anos*12)
if prestacao <= salario*30/100:
    print('Sua prestação será de \033[1:34m R${:.2f} \033[m.'.format(prestacao))
else:
    print('Não poderemos lhe fazer um empréstimo.')
