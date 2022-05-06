# termo1 = int(input('Qual o primeiro termo da PA? '))
# razão = int(input('Qual a razão da PA? '))
# for c in range(termo1,termo1+(10-1)*razão,razão): #achei esse jeito pior, pois não aceita números float
#     print('{}'.format(c), end=' -> ')
# print('ACABOU')
termo1 = float(input('Qual o primeiro termo da PA? '))
razão = float(input('Qual a razão da PA? '))
for c in range(0,10):
    #print('O {}º termo dessa PA é {:.1f}'.format(c+1, termo1+c*razão))
    print('{:.2f}'.format(termo1+c*razão), end=' -> ')
print('ACABOU')

