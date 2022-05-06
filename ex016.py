import math
num = float(input("Digite um número real qualquer: "))
inteiro = math.trunc(num)
print("A parte inteira de {:.3f} é {}".format(num, inteiro))
print(f'A parte inteira de {num:.3f} é {inteiro}')
