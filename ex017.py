import math
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("E do cateto adjacente: "))
hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
hipotenusa2 = math.hypot(cateto_oposto, cateto_adjacente)
print("A hipotenusa desse triângulo é {:.2f}".format(hipotenusa))
print(f"A hipotenusa desse triângulo é {hipotenusa2:.2f}")

