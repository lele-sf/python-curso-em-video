def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    tam = len(num)
    valores = ' '.join(str(n) for n in num)
    if tam == 0:
        valores = ''
        maior_valor = None
    else:
        maior_valor = max(num)
    print(f'{valores} Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maior_valor}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
