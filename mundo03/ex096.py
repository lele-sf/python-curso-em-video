def calcular_area(l, c):
    return l * c

print('Controle de Terrenos')
print('-' * 20)

larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

area = calcular_area(larg, comp)

print(f'A área de um terreno {larg}x{comp} é de {area}m²')
