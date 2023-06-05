nome = []
peso = []
maior_peso = []
menor_peso = []

while True:
    nome.append(input('Nome: '))
    peso.append(float(input('Peso: ')))
    escolha = input('Quer continuar? [S/N] ').upper()

    if peso[-1] >= 100:
        maior_peso.append(nome[-1])
    elif peso[-1] <= 70:
        menor_peso.append(nome[-1])

    if 'N' in escolha:
        break

print(f'Ao todo, você cadastrou {len(nome)} pessoas.')
print(f'O maior peso foi de {max(peso):.2f}Kg. Peso de {", ".join(maior_peso)}.')
print(f'O menor peso foi de {min(peso):.2f}Kg. Peso de {", ".join(menor_peso)}.')