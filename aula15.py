n = s = 0
while True:
    n = int(input('Digite um número: [999 para parar] '))
    if n == 999:
        break #Issa interrupção evita fazer a cambiarra s-999
    s += n
#print('A soma vale {}.'.format(s))
print(f'A soma vale {s}.') #Essa forma de escrever (f string) foi incluída à partir do Python 3.6

nome = 'Luís'
idade = 44
salário = 3043.43
print(f'O \033[31m{nome:^10}\033[m tem {idade} e ganha {salário:.1f}')
print(f'O \033[31m{nome:*^10}\033[m tem {idade} e ganha {salário:.1f}')
