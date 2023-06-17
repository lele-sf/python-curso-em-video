def leiaInt(n):
    while True:
        num = input(n)
        if num.isdigit():
            return int(num)
        else:
            print('ERRO! Digite um número inteiro válido.')

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
