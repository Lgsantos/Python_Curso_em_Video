n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1+n2)/2
if media < 5:
    print('A média do aluno é {:.1f} e ele foi reprovado.'.format(media))
elif media >=5 and media <= 6.9:
    print('A média do aluno é {:.1f} e ele está de recuperação.'.format(media))
else:
    print('A média do aluno é {:.1f} e ele está aprovado.'.format(media))
