r1 = float(input('Digite comprimento reta 1: '))
r2 = float(input('Digite comprimento reta 2: '))
r3 = float(input('Digite comprimento reta 3: '))
if abs(r2-r3) < r1 < (r2+r3):
    if abs(r1-r3) < r2 < (r1+r3):
        if abs(r1-r2) < r3 < (r1+r2):
            print('{}, {} e {} formam um triângulo'.format(r1, r2, r3))
        else:
            print('{}, {} e {} não formam um triângulo'.format(r1, r2, r3))
    else:
        print('{}, {} e {} não formam um triângulo'.format(r1, r2, r3))
else:
    print('{}, {} e {} não formam um triângulo'.format(r1, r2, r3))