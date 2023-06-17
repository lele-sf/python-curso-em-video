from random import randint

numeros = []

def sorteio():
    print('Sorteando 5 valores da lista:', end=' ')
    for _ in range(5):
        num_aleatorio = randint(0, 10)
        numeros.append(num_aleatorio)
        print(num_aleatorio, end=' ')
    print('PRONTO!')

def somaPar():
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'Os valores pares de {numeros}, temos {soma}')

sorteio()
somaPar()