nome = str(input('Qual é o seu nome completo? ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
prenome = nome.split()
print(len(prenome[0]))
