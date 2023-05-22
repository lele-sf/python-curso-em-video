maior_idade = 0
menor_idade = 0
nome_mais_velho = ''
soma = 0
menor_20 = 0

for i in range(1,5):
    print(f'----- {i}° PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').lower()
    soma += idade

    if i == 1:
        maior_idade = idade
        menor_idade = idade
        if sexo == 'm':
            nome_mais_velho = nome
    if idade > maior_idade:
        maior_idade = idade
        nome_mais_velho = nome
    if idade < menor_idade:
        menor_idade = idade
    if idade < 20 and sexo == 'f':
        menor_20 += 1

media = soma / 4
print(f'A média de idade do grupo é de {media} anos\nO homem mais velho tem {maior_idade} anos e se chama {nome_mais_velho}\nAo todo são {menor_20} mulheres com menos de 20 anos')