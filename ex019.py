from random import choice

alunos = []
for i in range(4):
    nome = (input(f"Digite o nome do estudante {i+1}: "))
    alunos.append(nome)

aluno_aleatorio = choice(alunos)

print("Aluno escolhido: ", aluno_aleatorio)