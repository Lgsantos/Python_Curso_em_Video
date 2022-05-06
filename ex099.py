def maior(* para):
    from time import sleep
    print('-=' * 40, '\nAnalisando parâmetros...')
    sleep(0.5)
    for v in para:
        print(f'{v}', end=' ')
        sleep(0.25)
    print(f'Foram informados {len(para)} valores ao todo.')
    sleep(0.5)
    if len(para) != 0:
        print(f'O maior valor foi {max(para)}.')
    else:
        print(f'O maior valor foi 0.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
