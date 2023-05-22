qntd_idade = 0
total_M = 0
total_F = 0

while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    if idade >= 18:
            qntd_idade += 1

    while sexo not in 'MF':
        sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        total_M += 1
    elif sexo == 'F' and idade < 20:
        total_F += 1

    user_choice = ' '
    while user_choice not in 'SN':
        user_choice = input('Digite [S/N] para continuar: ').upper().strip()[0]
    if user_choice == 'S':
        continue
    elif user_choice == 'N':
        break

print(f'Quantidade de pessoas maior que 18 anos: {qntd_idade}\nAo todo temos {total_M} homens cadastrados\nE temos {total_F} mulheres com menos de 20 anos')