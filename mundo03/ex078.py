lista = []

for _ in range(5): 
    lista.append(int(input('Digite um número: ')))

maior = max(lista)
menor = min(lista)

indices_maior = [i+1 for i, num in enumerate(lista) if num == maior]
indices_menor = [i+1 for i, num in enumerate(lista) if num == menor]

print(f'Você digitou os valores {lista}')
print(f'O maior número digitado foi {maior} nas posições {indices_maior}')
print(f'O menor número digitado foi {menor} nas posições {indices_menor}')
