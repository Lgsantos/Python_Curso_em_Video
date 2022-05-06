# VARIÁVEIS COMPOSTAS: LISTAS (PARTE 1) - AO CONTRÁRIO DAS TUPLAS, LISTAS SÃO MUTÁVEIS.
# USAMOS [] PARA DEFINÍ-LAS (AO INVÉS DE "()" DAS TUPLAS)
# É POSSÍVEL ADICIONAR MAIS ELEMENTOS EM UMA LISTA (em seu final) COM O MÉTODO APPEND: lista.append('novo')
# PARA ADICIONAR NOVO ELEMENTO EM UMA POSIÇÃO ESPECÍFICA DA LISTA, USA-SE O MÉTODO INSERT: lista.insert(0,'novo')
# PARA APAGAR UM ELEMENTO DA LISTA PODEMOS USAR:
#   O COMANDO DEL: del lista[3]
#   O MÉTODO POP: lista.pop(3) - apaga o 3º elemento a partir do último; lista.pop(3,0) inverte
#           lista.pop() remove o último elemento da lista
#   O MÉTODO REMOVE: lista.remove('novo') apaga o elemento 'novo' da lista
#           se tentar remover elemento inexistente na lista, ocorre erro. Para evitar
#           isso, podemos usar IF e IN: IF 'novo' IN lista: lista.remove('novo')
# APÓS UMA DELEÇÃO, A NUMERAÇÃO DOS ELEMENTOS DA LISTA É REFEITA (NÃO FICAM ESPAÇOS VAZIOS)
# PARA CRIAR UMA LISTA NUMÉRICA, PODEMOS UTILIZAR O RANGE: lista = list(range(4,11))
# PARA ORDENAR OS ELEMENTOS DE UMA LISTA: lista.sort() e na forma inversa: lista.sort(reverse=True)
# PARA DETERMINAR O TAMANHO DE UMA LISTA: len(lista)
lista = [2,5,8,3]
# lista = list(2,5,8,3) # outro jeito para se criar uma lista
print(lista)
lista[2] = 1    # listas são mutáveis
print(lista)
# lista[4] = 7    # não é assim que se inclui um novo elemento na lista
lista.append(7)   # é assim
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
print(f'Essa lista tem {len(lista)} elementos')
lista.insert(2,0)
print(lista)
lista.pop()
print(lista)
lista.pop(2)
print(lista)
lista.insert(2,2)
print(lista)
lista.remove(2) # removeu apenas o primeiro elemento 2, da esquerda para a direita.
print(lista)    # usar um laço para remover mais de um elemento igual
if 4 in lista: lista.remove(4)
else: print('A lista não tem o número 4')
valores = []
valores.append(5)
valores.append(3)
valores.append(1)
print(valores)
for v in valores:
    print(f'{v}...',end='')
print()
# for cont in range(0,3):
#     valores.append(int(input('Digite um valor: ')))
# print(valores)
a = [2,4,5,8]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2]=3 # no python, quando atribuímos uma lista a uma variável, elas ficam ligadas!
# o que acontece com uma, acontece com a outra
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print()
a = [2,4,5,8]
b = a[:] # essa é a forma para se copiar a lista a, sem ligá-la à lista b
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2]=3 # no python, quando atribuímos uma lista a uma variável, elas ficam ligadas!
# o que acontece com uma, acontece com a outra
print(f'Lista A: {a}')
print(f'Lista B: {b}')
lista2 = [2,5,8,1,2,8]
for p, l in enumerate(lista2):
    if l == max(lista2): print(f'{p}...',end='')





