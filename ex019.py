import random
aluno01 = input("Digite o nome do aluno: ")
aluno02 = input("Digite o nome do aluno: ")
aluno03 = input("Digite o nome do aluno: ")
aluno04 = input("Digite o nome do aluno: ")
lista = [aluno01,aluno02,aluno03,aluno04]
escolhido = random.choice(lista)
print("O aluno escolhido para limpar o quadro negro foi {}"\
      .format(escolhido))

