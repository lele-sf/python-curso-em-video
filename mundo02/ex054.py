import time
ano_atual = time.localtime().tm_year
total_maior = 0
total_menor = 0

for i in range(0,7):
    ano_nasc = int(input(f'Digite o {i+1}° ano de nascimento: '))
    idade = ano_atual - ano_nasc

    if idade > 18:
        total_maior += 1
    else:
        total_menor += 1

print(f'Ao todo tivemos {total_maior} pessoas maiores de idade\nE também tivemos {total_menor} menores de idade')
