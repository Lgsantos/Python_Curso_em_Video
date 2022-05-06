altura = float(input('Qual é sua altura em metros? '))
peso = float(input('Qual é seu peso em Kg? '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Seu IMC é \033[1;33m{:.1f}\033[m: você está ABAIXO DO PESO.'.format(imc))
elif 18.5 <= imc <= 25: #Poucas linguagens aceitam a fórmula à esquerda. imc >= 18.5 and imc <= 25
    print('Seu IMC é \033[1;33m{:.1f}\033[m: você está no PESO IDEAL.'.format(imc))
elif 25 < imc <= 30: #Essa é uma das vantagens do Python. imc > 25 and imc <= 30
    print('Seu IMC é \033[1;33m{:.1f}\033[m: você está com SOBREPESO.'.format(imc))
elif 30 < imc <= 40: #As fórmulas podem se parecer como nas expressões matemáticas.
    print('Seu IMC é \033[1;33m{:.1f}\033[m: você está com OBESIDADE.'.format(imc))
else:
    print('Seu IMC é {:.1f}. Você está com OBESIDADE MÓRBIA.'.format(imc))

