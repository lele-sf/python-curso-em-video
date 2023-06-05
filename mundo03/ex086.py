matriz = []

for l in range(3):
    linha = []
    for c in range(3):
        valor = int(input(f'Digite o valor para a posição ({l}, {c}): '))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        print(f'[ {elemento} ]',end=' ')
    print()