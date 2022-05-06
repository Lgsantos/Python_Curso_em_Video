#   MÓDULOS E PACOTES: Modularização - criar módulos. Comoçou por volta anos 1960, quando os programas
#                                       começaram a ficar muito grandes, dificultando entendimento e leitura
#                                       dos mesmos.
#                                       Objetivo 1: dividir um programa grande
#                                       Objetivo 2: aumentar legibilidade dos programas
#                                       Objetivo 3: + fácil encontrar erros e fazer melhorias / manutenção.
#                                       Vantagem 1: Organização do código
#                                       Vantagem 2: Facilita manutenção
#                                       Vantagem 3: Ocultação de código detalhado
#                                       Vantagem 4: Reutilização de módulos em outros projetos
#                       Pacotes - Quando os módulos não resolverem mais o problema, por terem ficado muito
#                               muito grandes, podemos utilizar os pacotes do Python (outras linguagens
#                               chamam-nos de bibliotecas.
#                               Pacotes são pastas que contêm módulos, separados por assuntos.
#                               Para importar o pacote inteiro: import <nome do pacote>;
#                               Para importar módulos específicos de um pacote: from <nome do pacote> import <nome do módulo>1,...
#                               Para criar pacotes e módulos, basta criar pastas dentro dos projetos, mas
#                               nas pastas precisa existir um arquivo chamado __init__.py (o PyCharm os cria automaticamente)
#import úteis # Todas as funções criadas foram salvas em úteis.py e podem ser importadas
# from úteis import fatorial, dobro, triplo # também poderiam ser importadas assim, evitando que sempre
#                                           #precisassemos digitar "úteis." O Python recomenda a primeira
#                                           #forma, pois no evita conflitos entre funções de módulos
#                                           #diferentes com o MESMO nome (quando isso ocorre, Python usa
#                                           #a última função importada.

# num = int(input('Digite um valor: '))
# fat = úteis.fatorial(num) # essa é a forma de chamar cada função individualmente
# print(f'O fatorial de {num} é {fat}.')
# print(f'O dobro de {num} é {úteis.dobro(num)}')
# print(f'O triplo de {num} é {úteis.triplo(num)}')
from uteis import números
num = int(input('Digite um valor: '))
fat = números.fatorial(num) # essa é a forma de chamar cada função individualmente
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {números.dobro(num)}')
print(f'O triplo de {num} é {números.triplo(num)}')