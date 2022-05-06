from uteis import strings, números #se criasse um diretório e uma pasta para organizar os packages/modulos, basta
#  usar from <nome do diretório>.<nome da pasta>.<nome do package> import * (ou os nomes dos módulos específicos)
sair = False
while True:
    strings.título('MENU PRINCIPAL'.center(38), 48)
    while True:
        opção = strings.menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
        # opção = números.leiaint('\033[0;32mSua opção: \033[m')
        if opção == 1:
            strings.título('OPÇÃO 1'.center(38), 48)
            try:
                f = open('115a.txt', 'r')
            except:
                f = open('115a.txt', 'w+')
            print(f.read(), end='')
            f.close()
            print('~'* 42)
        elif opção == 2:
            strings.título('NOVO CADASTRO'.center(38), 48)
            nome = input('Nome: ')
            idade = input('Idade: ')
            linha = f'{nome:<35}{idade:>2} anos\n'
            f = open('115a.txt', 'a')
            f.write(linha)
            f.close()
            print('~' * 42)
        elif opção == 3:
            print('\033[0;36mATÉ LOGO! TENHA UM ÓTIMO DIA!\033[m')
            sair = True
            break
        else:
            print('\033[0;31mERRO! Digite uma opção válida!\033[m')
            break
    if sair:
        break