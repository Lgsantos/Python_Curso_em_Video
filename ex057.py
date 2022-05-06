# sexo = ' '
# while sexo not in 'MF':
#     sexo = input('Digite seu sexo: [M/F] ').upper().strip()

sexo = input('Digite seu sexo: [M/F] ').upper().strip()
while sexo not in 'MF':
    print('Opção inválida!')
    sexo = input('Digite seu sexo: [M/F] ').upper().strip()