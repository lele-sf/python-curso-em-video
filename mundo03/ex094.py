pessoas = []

while True:
    pessoa = {}

    nome = input('Nome: ')
    sexo = input('Sexo: [F/M] ').upper()
    if sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        continue
    idade = int(input('Idade: '))

    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade

    pessoas.append(pessoa)

    escolha = input('Quer continuar? [S/N] ').upper()

    if escolha == 'N':
        break

print('-='*25)
tot_pessoas = len(pessoas)
print(f' - O grupo tem {tot_pessoas} pessoas.')

idades = [pessoa['idade'] for pessoa in pessoas]
media = sum(idades) / tot_pessoas
print(f' - A média de idade é de {media:.2f} anos.')

mulheres = []
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
mulher = ', '.join(mulheres)
print(f' - As mulheres cadastradas foram: {mulher}')

print(' - Lista de pessoas que estão acima da média:')
acima_media = []
for pessoa in pessoas:
    if pessoa['idade'] > media:
        acima_media.append(pessoa)
for pessoa in acima_media:
    nome = pessoa['nome']
    idade = pessoa['idade']
    sexo = pessoa['sexo']
    print(f'Nome: {nome}, Sexo: {sexo}, Idade: {idade}')
