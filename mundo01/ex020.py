from random import shuffle

alunos = []
for i in range(4):
    nome = (input(f"Digite o nome do estudante {i+1}: "))
    alunos.append(nome)

shuffle(alunos)

print("Ordem dos alunos escolhidos: ", alunos)