num_set = set()

while True:
    num = int(input('Digite um número: '))
    escolha = input('Você deseja continuar [S/N]? ').upper()

    num_set.add(num)
    if escolha == 'N':
        break

lista = sorted(num_set)

print(lista)
