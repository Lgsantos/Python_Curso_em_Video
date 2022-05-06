preco_inicial = int(input("Qual o preço do produto em reais? "))
desconto = 5 # em %
preco_final = preco_inicial * (1 - (desconto / 100))
print("O preço final do produto, com desconto de {}% é de {:.2f} reais.".format(desconto, preco_final))