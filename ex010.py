reais = int(input("Quantos reais você tem na carteira? "))
dolares = int(reais // 3.27)
cents = int((reais % 3.27) / 3.27 * 100)
print("Com {} reai(s) você pode comprar {} dólar(es) e {} centavo(s) de dólar.".format(reais, dolares, cents),"\n"
      "Cotação: US$ 1,00 = R$ 3,27")
