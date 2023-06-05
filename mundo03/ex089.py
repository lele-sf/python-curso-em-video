alunos = [
    {'nome': [], 'nota1': [], 'nota2': []}
]

while True:
    alunos[0]['nome'].append(input('Nome: '))
    alunos[0]['nota1'].append(float(input('Nota 1: ')))
    alunos[0]['nota2'].append(float(input('Nota 2: ')))
    escolha = input('Quer continuar? [S/N] ').upper()

    if escolha == 'N':
        break

print("-" * 30)
print(f'{"No.": <4}{"NOME": <10}{"MÉDIA": <6}')
print("-" * 30)

for i, aluno in enumerate(alunos[0]['nome']):
    nota1 = alunos[0]['nota1'][i]
    nota2 = alunos[0]['nota2'][i]
    media = (nota1 + nota2) / 2

    print(f'{i+1: <4}{aluno: <10}{media:.1f}')

print("-" * 30)
while True:
    num_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num_aluno == 999:
        break
    elif num_aluno > 0 and num_aluno <= len(alunos[0]['nome']):
        indice_aluno = num_aluno - 1
        nome_aluno = alunos[0]['nome'][indice_aluno]
        notas_aluno = (alunos[0]['nota1'][indice_aluno], alunos[0]['nota2'][indice_aluno])
        print(f'Notas de {nome_aluno} são {notas_aluno}')
    else:
        print('Aluno não encontrado.')