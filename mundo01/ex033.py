numeros = []

for i in range(3):
    num = int(input('Digite um número: '))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)

print(f'O número {maior} é o maior e {menor} é o menor')
