def leiadinheiro(str):
    while True:
        num = input(f'{str}').strip()
        vírgula = False
        if ','in num:
            num = num.replace(',', '.')
            vírgula = True
        numeric = True
        for d in num:
            if d not in '0123456789.':
                numeric = False
        if numeric:
            return float(num)
        print(f'\033[1;31m{num} não é um valor válido!\033[m')
