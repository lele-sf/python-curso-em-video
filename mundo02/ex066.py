cont = 0
soma = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Quantidade de números digitados: {cont}\nSoma total: {soma}')