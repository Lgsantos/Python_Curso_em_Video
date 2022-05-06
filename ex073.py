brasileirão2017 = ('Corinthians', 'Palmeiras','Santos','Grêmio','Cruzeiro',
                   'Flamengo','Vasco da Gama','Chapecoense','Atlético Mineiro',
                   'Botafogo','Athletico-PR','Bahia','São Paulo','Fluminense',
                   'Sport Recife','Vitória','Coritiba','Avaí','Ponte Preta',
                   'Atlético Goianiense')
print('-='*18)
print(f'Lista dos clubes do Brasileirão 2017: {brasileirão2017}')
print('-='*18)
print(f'Os 5 primeiros clubes são: {brasileirão2017[:5]}')
print('-='*18)
print(f'Os 4 últimos clubes são: {brasileirão2017[-4:]}')
print('-='*18)
print(f'Clube em ordem alfabética: {sorted(brasileirão2017)}')
print('-='*18)
print(f'A Chapecoense ficou na {brasileirão2017.index("Chapecoense")+1}ª colocação')
