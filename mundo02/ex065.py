soma = 0
cont = 0
maior = float('-inf')
menor = float('inf')
continuar = True

while continuar:
    num = int(input("Digite um número inteiro: "))

    soma += num
    cont += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num

    opcao = input("Deseja continuar? (S/N) ").upper()
    if opcao != "S":
        continuar = False

media = soma / cont

print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")