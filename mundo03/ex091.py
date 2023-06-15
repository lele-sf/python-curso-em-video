from random import randint
from time import sleep

jogadores = {'jogador1':[],'jogador2':[],'jogador3':[],'jogador4':[]}

print('Valores sorteados: ')
for jogador in jogadores:
    num_aleatorio = randint(1,6)
    jogadores[jogador].append(num_aleatorio)
    print(f"  O {jogador} tirou {num_aleatorio}")
    sleep(0.7)

print('== RANKING DOS JOGADORES == ')

sorted_jogadores = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

for posicao, (jogador, valor) in enumerate(sorted_jogadores, start=1):
    print(f'  {posicao}º lugar: {jogador} com {valor[0]}')
    sleep(0.7)
