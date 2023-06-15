estudante = {}

nome = input('Nome: ')
media = float(input(f'Média de {nome}: '))

if media > 6:
    situacao = 'Aprovado(a)!'
elif 5 <= media <= 6:
    situacao = 'Recuperação!'
else:
    situacao = 'Reprovado(a)!'

estudante['nome'] = nome
estudante['media'] = media
estudante['situacao'] = situacao

print('Dados do estudante:')
for chave, valor in estudante.items():
    print(f' - {chave}: {valor}')