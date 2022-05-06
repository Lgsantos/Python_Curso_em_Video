import math
angulo = math.radians(float(input("Digite um ângulo: ")))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print("Para o ângulo {:.2f} temos:\nseno = {:.2f}".format(math.degrees(angulo),seno),
      "\ncosseno = {:.2f}\n".format(cosseno),
      "tangente = {:.2f}".format(tangente))
print(f"Para o ângulo {math.degrees(angulo):.2f} temos:\nseno = {seno:.2f}"
      f"\ncosseno = {cosseno:.2f}\n"
      f"tangente = {tangente:.2f}")
