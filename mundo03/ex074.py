import random

tupla = []

while True:
    num_aleatorio = random.randint(1,10)
    tupla.append(num_aleatorio)

    if len(tupla) == 5:
        break

print(f'Os valores sorteados foram {tupla}')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')