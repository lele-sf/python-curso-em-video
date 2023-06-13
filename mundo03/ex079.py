lista = []

while True:
    num = int(input('Digite um valor: '))
    escolha = input('Quer continuar? [S/N] ').upper()
    
    if num in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(num)

    if escolha == 'N':
        break

print(f'Você digitou os valores {sorted(lista)}')