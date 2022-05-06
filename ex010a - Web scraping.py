from bs4 import BeautifulSoup
import requests

# O site principal é https://www.bcb.gov.br/estabilidadefinanceira/fechamentodolar, mas tive que
#procurar a URL que continha as cotações
URL = 'https://ptax.bcb.gov.br/ptax_internet/consultarUltimaCotacaoDolar.do'
# para obter o agent do browser, basta pesquisar 'my browser agent', copiar o resultado e colar no dicionário abaixo
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')
# cotacao_texto = soup.find('td', align="right")
# cotacao = float(cotacao_texto.text.replace(',', '.'))
cotacao2_texto = soup.find('tr', class_='fundoPadraoBClaro2').text
cotacao2 = float(cotacao2_texto[-7:].replace(',', '.'))
reais = int(input("Quantos reais você tem na carteira? "))
dolares = int(reais // cotacao2)
cents = int((reais % cotacao2) / cotacao2 * 100)

data_cotacao = soup.find('td', align='CENTER')

print("Com {} reai(s) você pode comprar {} dólar(es) e {} centavo(s) de dólar.".format(reais, dolares, cents),"\n"
      "Cotação do dia {}: US$ 1,00 = R$ {:.2f}".format(data_cotacao.text, cotacao2))
