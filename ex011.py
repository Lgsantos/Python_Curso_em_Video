largura = int(input("Qual a largura da parede em metros? "))
altura = int(input("Qual a altura da parede em metros? "))
area = largura * altura
rendimento = 2 # 1 litro de tinta pinta 2 m^2
litros = area / rendimento
print("Sua parede tem {} metros quadrados e são necessários {} litros".format(area, litros),
      "de tinta para pintá-la.")
