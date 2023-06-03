lista = []

for _ in range(5): 
    num = int(input('Digite um número: '))
    lista.append(num)

    if num == max(lista): 
        posicao = len(lista) - 1
    elif num == min(lista):
        posicao = 0
    else:
        posicao = lista.index(num)

    print(f'Adicionado na posição {posicao} da lista...')

lista_ordenada = sorted(lista)
print(f'Os valores digitados em ordem foram {lista_ordenada}')