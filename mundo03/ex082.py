lista = []
pares = []
impar = []

while True:
    try:
        num = int(input('Digite um número: '))
        escolha = input('Você deseja continuar [S/N]? ').upper()
        
        if num in lista:
            print('Valor duplicado! Não vou adicionar...')
        else:
            lista.append(num)
            if num % 2 == 0:
                pares.append(num)
            else:
                impar.append(num)

        if escolha == 'N':
            break

    except ValueError:
        print('Entrada inválida. Por favor, digite um número válido.')
        continue

print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impar}')