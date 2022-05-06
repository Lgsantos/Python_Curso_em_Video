salario_atual = int(input("Qual o salário atual? "))
aumento = 15 # em %
salario_final = salario_atual * (1 + aumento / 100)
print("O salário final, após aumento de {}% é de {} reais.".format(aumento, salario_final))