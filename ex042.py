r1 = float(input('Digite comprimento reta 1: '))
r2 = float(input('Digite comprimento reta 2: '))
r3 = float(input('Digite comprimento reta 3: '))
if abs(r2-r3) < r1 < (r2+r3):
    if abs(r1-r3) < r2 < (r1+r3):
        if abs(r1-r2) < r3 < (r1+r2):
            print('{}, {} e {} formam um triângulo'.format(r1, r2, r3))
            if r1 == r2 == r3: #também poderia ser escrito r1 == r2 and r2 == r3
                print('O triângulo formado é equilátero.')
            elif (r1 == r2 != r3) or (r3 == r2 != r1):#(r1 == r2 and r2 != r3) or (r2 == r3 and r2 != r1)
                print('O triângulo formado é isósceles.')
            else:
                print('O triângulo formado é escaleno.')
        else:
            print('{}, {} e {} não formam um triângulo'.format(r1, r2, r3))
    else:
        print('{}, {} e {} não formam um triângulo'.format(r1, r2, r3))
else:
    print('{}, {} e {} não formam um triângulo'.format(r1, r2, r3))