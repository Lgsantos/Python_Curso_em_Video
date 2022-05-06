lista = []
conta_abre = conta_fecha = 0
expressão = input('Digite uma expressão matemática usando parênteses: ').strip()
for l in expressão:
    lista.append(l)
# abre_parenteses = lista.count('(')   # fiz esse código, mas logo percebi que poderia melhorá-lo
# fecha_parenteses = lista.count(')')
# if abre_parenteses == fecha_parenteses:
#     print('Expressão é válida!')
# else:
#     print('Expressão não é válida!')
for l in lista:
    if l == '(':
        conta_abre += 1
    if l == ')':
        conta_fecha += 1
        if conta_abre < conta_fecha:
            print('Expressão não é válida!')
            break
if conta_abre == conta_fecha:
    print('Expressão é válida!')
else:
    print('Expressão não é válida!')