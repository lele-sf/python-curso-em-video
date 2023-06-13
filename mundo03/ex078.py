lista_num = []
maior_pos = []
menor_pos = []

for i in range(5):
    num = int(input(f'Digite um valor para a Posição {i}: '))
    lista_num.append(num)

maior = max(lista_num)
menor = min(lista_num)

for index, num in enumerate(lista_num):
    if num == maior:
        maior_pos.append(index)
    elif num == menor:
        menor_pos.append(index)

print(f'Você digitou os valores {lista_num}')
print(f'O maior valor digitado foi {maior} nas posições {maior_pos}')
print(f'O menor valor digitado foi {menor} nas posições {menor_pos}')