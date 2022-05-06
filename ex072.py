extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
           'nove','dez','onze','doze','treze','quatorze','quinze',
           'dezesseis','dezessete','dezoito','dezenove','vinte')
# while True:
#     num = int(input('Digite um número inteiro de 0 a 20: '))
#     if num in range(0,21):
#         break
#     print('Número inválido! Tente novamente.')
# print(f'Você digitou o número {extenso[num]}')
#
# DESAFIO: ALTERAR PROGRAMA ACIMA PARA PERGUNTAR SE USUÁRIO DESEJA CONTINUAR
sair = False
while True:
    while True:
        num = int(input('Digite um número inteiro de 0 a 20: '))
        if num in range(0,21):
            print(f'Você digitou o número {extenso[num]}')
            cont = input('Deseja continuar? [S/N] ').upper().strip()
            if cont == 'S': break
            else: sair = True
        if not sair:
            print('Número inválido! Tente novamente.')
        break
    if sair: break
