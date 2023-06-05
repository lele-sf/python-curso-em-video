num = {'par': [], 'impar': []}

for i in range(1, 8):
    n = int(input(f'Digite o {i}° valor: '))

    if n % 2 == 0:
        num['par'].append(n)
    else:
        num['impar'].append(n)

num['par'] = sorted(num['par'])
num['impar'] = sorted(num['impar'])

print(f'Números pares: {num["par"]}')
print(f'Números ímpares: {num["impar"]}')