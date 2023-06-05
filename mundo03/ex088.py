from random import randint

jogos = []
num_sort = []

print(f'{"-"*33}\n\tJOGO NA MEGA SENA\n{"-"*33}')
qntd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

for _ in range(qntd_jogos):
    jogo = []
    for _ in range(6):
        jogo.append(randint(0, 60))
    jogos.append(jogo)

print(f'{"-="*3} SORTEANDO {qntd_jogos} JOGOS {"-="*3}')
for i, jogo in enumerate(jogos):
    print(f'Jogo {i+1}: {jogo}')