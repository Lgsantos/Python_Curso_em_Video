#   VARIÁVEIS COMPOSTAS - LISTAS (PARTE 2): dominar estrutura de dados aumenta a gama de coisas que podemos fazer com
#                                           nossos programas.
teste = []
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = []
# galera.append(teste)
# print(galera)
# teste[0]='Maria'
# teste[1]=22
# galera.append(teste)
# print(galera)   # O append está ligando as listas. Para evitar isso precisamos de [:] para copiar apenas o conteúdo
galera.append(teste[:])
print(galera)
teste[0]='Maria'
teste[1]=22
galera.append(teste[:])
print(galera)
galera = [['Bruno', 16], ['Pedro', 10], ['Felipe', 5], ['Gustavo', 43]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[0][1])
for p in galera:
    print(p)
for p in galera:
    print(p[0])
for p in galera:
    print(p[1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')
dado = []
for i in range(0,3):
    dado.append(input('Digite um nome: '))
    dado.append(int(input('Digite uma idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1]<=18: print(f'{p[0]} é menor de idade')