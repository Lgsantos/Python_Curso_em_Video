#   TRATAMENTO DE ERROS E EXCEÇÕES: estrutura try:<operação> except:<falhou> else:<deu certo> finally:<certo/falha>
#                                   cada try: pode ter vários except: para tratar mais de um tipo de erro
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except:
#     print('Infelizmente tivemos um problema... :(')
# except Exception as erro:
#     print(f'O erro encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um erro com os tipos de dados que você digitou!')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else:       # sem o else: o último print seria mostrado, e o usuário veria a mensagem do erro (divisão por zero)
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado!')