while True:
    num = int(input('Digite um número para saber sua tabuada: '))

    if num < 0:
        break

    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')

