lista = []

while True:
    try:
        num = int(input('Digite um número: '))
        escolha = input('Você deseja continuar [S/N]? ').upper()
        lista.append(num)
    except ValueError:
        print('Entrada inválida. Por favor, digite um número válido.')
        continue

    if escolha == 'N' or escolha == 'NÃO':
        break

lista.sort(reverse=True)

print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')
