# CORES NO TERMINAL (existem inúmeros módulos (e.x.: colorize) mas aqui será explicado o básico
# ANSI escape sequence \033[m
# e.x.: \033[<STYLE>;<TEXT>;<BACKGROUND>m
# e.x.: \033[0;33;44m
# STYLE: 0 = NONE; 1 = BOLD; 4 = UNDERLINE; 7 = NEGATIVE
# TEXT: 30 = WHITE; 31=RED; 32=GREEN; 33=YELLOW; 34=BLUE; 35=MAGENTA; 36=CYAN; 37=GRAY
# BACKGROUND: 40 = WHITE; 41=RED; 42=GREEN; 43=YELLOW; 44=BLUE; 45=MAGENTA; 46=CYAN; 47=GRAY

print('\033[31mOlá mundo')
print('\033[7;31mOlá mundo\033[m')
print('\033[31;43mOlá mundo')
print('\033[1;31;43mOlá mundo')
print('\033[31;43mOlá mundo\033[m')
print('\033[4;30;45mOlá mundo\033[m')
print('\033[7;30;45mOlá mundo\033[m')
a = 3
b = 5
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))
print('Os valores são \033[1;32;40m{}\033[m e \033[1;31;40m{}\033[m'.format(a, b))
print('Os valores são \033[7;32;40m{}\033[m e \033[7;31;40m{}\033[m'.format(a, b))
print('Os valores são {}{}{} e {}{}{}'.format('\033[32m', a, '\033[m', '\033[31m', b, '\033[m'))
print('Os valores são {}{}{} e {}{}{}'.format(cores['pretoebranco'], a, cores['limpa'], cores['amarelo'], b, cores['limpa']))
