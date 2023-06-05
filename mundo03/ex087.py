matriz = []
soma_par = 0
soma_col = 0

for l in range(3):
    linha = []
    for c in range(3):
        valor = int(input(f'Digite o valor para a posição ({l}, {c}): '))
        linha.append(valor)
        if c == 2:
            soma_col += valor
    matriz.append(linha)

maior = max(matriz[1])

print('-='*15)
for linha in matriz:
    for elemento in linha:
        print(f'[ {elemento} ]', end=' ')
        if elemento % 2 == 0:
            soma_par += elemento
    print()
print('-='*15)

print(f'A soma dos valores pares é {soma_par}.')
print(f'A soma dos valores da terceira coluna é {soma_col}.')
print(f'O maior valor da segunda linha é {maior}.')
