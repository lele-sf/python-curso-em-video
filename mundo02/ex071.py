valor_saque = int(input('Digite o valor a ser sacado: R$ '))

cedulas = [50, 20, 10, 1]  # Valores das cédulas disponíveis
quantidades = [0, 0, 0, 0]  # Quantidades de cada cédula

i = 0  # Índice para percorrer a lista de cédulas

while valor_saque > 0:               # 2321 > 0 == True
    if valor_saque >= cedulas[i]:    # 2321 >= cedulas[0] == True
        quantidades[i] = valor_saque // cedulas[i] #qtnd[0] == 2321 // cedulas[0] == 46
        valor_saque %= cedulas[i]    # 2321 = 2321 % cedulas[0] == 21
    i += 1

print('Quantidade de cédulas:')
for j in range(len(cedulas)):
    print(f'Cédulas de R${cedulas[j]}: {quantidades[j]}')