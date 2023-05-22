nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Média: {media:.1f}')

if media < 5:
    print('REPROVADO')
elif media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')