frase = 'Curso em Vídeo Python'
# FATIAMENTO DE STRING
print(frase[3:])
print(frase[:7])
print(frase[2:9])
print(frase[3:15:2])
print(frase[::3])

# IMPRIMINDO TEXTOS LONGOS
print("""Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações 
com replace(), upper(), lower(), capitalize(), title(),
strip(), junção com join().""")

# ANALIZANDO A STRING
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print('Curso' in frase)
print(frase.find('em')) #retorna a posição inicial da string procurada na string maior
print(frase.find('ameba')) #retorna -1 se não encontra string procurada na string maior

# TRANSFORMANDO A STRING
print(frase.upper())
print(frase.lower())
print(frase.replace('Python','Android   '))
print(len(frase.replace('Python','Android   '))) #O replace altera a instância da string, mas ela é imutável.
                                                # Assim, print(frase) após replace daria o valor original da string
                                                #Só mudaria se houvesse atribuição, como abaixo
frase = frase.replace('Python','Android   ')
print(frase)
print(len(frase.strip()))
print(frase.split())
print(frase.split(' '))
print(frase.strip().split(' '))
dividido = frase.split()
print(dividido[0])
print(dividido[1])
print(dividido[3])
print(dividido[2][3])
print(dividido[3][2:])

