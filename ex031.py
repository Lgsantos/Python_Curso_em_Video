km = int(input('Digite a distância da viagem em km: '))
print('O preço da passagem será {} reais'.format(km*0.50) if km <= 200 else\
      'O preço da passagem será {} reais'.format(km*0.45))
