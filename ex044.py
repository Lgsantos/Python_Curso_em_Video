print('{:=^50}'.format(' LOJAS SANTOS '))
normal = float(input('Qual o preço normal do produto? '))
condicao = float(input('Qual a condição de pagamento?\n'
                       'Digite 1 para pagamento À VISTA com DINHEIRO ou CHEQUE\n'
                       'Digite 2 para pagamento À VISTA no CARTÃO\n'
                       'Digite 3 para pagamento À PRAZO até 2X no CARTÃO\n'
                       'Digite 4 para pagamento À PRAZO 3x ou mais no CARTÃO\n'
                       'Escolha: '))
if condicao == 1:
    print('O preço final do produto é \033[32mR${:.2f}\033[m.'.format(normal * 90/100))
elif condicao == 2:
    print('O preço final do produto é \033[32mR${:.2f}\033[m.'.format(normal * 95/100))
elif condicao == 3:
    print('O preço final do produto é \033[32mR${:.2f}\033[m.'.format(normal))
else:
    print('O preço final do produto é \033[32mR${:.2f}\033[m.'.format(normal * 120/100))