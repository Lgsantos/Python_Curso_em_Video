palavras = ('Aprender','Programar','linguagem','python','curso','gratis',
            'estudar','praticar','trabalhar','mercado','programador','futuro')
vogais = ('a','e','i','o','u')
for p in palavras:
    print(f'Na palavra {p.upper()} temos ', end='')
    for l in p:
        if l in vogais: print(l, end=' ')
    print()