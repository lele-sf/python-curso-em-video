dist_viagem = int(input('Digite a distância da viagem (Km): '))

if dist_viagem <= 200:
    preco_passagem = dist_viagem * 0.5
    print(f'Preço da passagem R${preco_passagem:.2f}')
else:
    preco_passagem = dist_viagem * 0.45
    print(f'Preço da passagem R${preco_passagem:.2f}')