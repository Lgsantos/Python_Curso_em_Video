cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('A cidade começa com "Santo"? {}'.format(cidade[:5].upper() == 'SANTO'))

#cidade = input('Digite o nome de uma cidade: ')
#cidade = cidade.strip().upper()
#if cidade.find('SANTO') == 0:
#    print('Cidade começa com "SANTO"')
#else:
#    print('Cidade não começa com "SANTO"')
