cadastro_jogador = {'nome': [], 'gols': [], 'total': []}

while True:
    nome = input('Nome do jogador: ')
    cadastro_jogador['nome'].append(nome)
    qntd_partidas = int(input(f'Quantas partidas {nome} jogou? '))

    gols_partidas = []

    for partida in range(qntd_partidas):
        gols = int(input(f'Quantos gols na partida {partida + 1}? '))
        gols_partidas.append(gols)

    total_gols = sum(gols_partidas)
    
    cadastro_jogador['gols'].append(gols_partidas)
    cadastro_jogador['total'].append(total_gols)
    break
print('-='*25)
print(cadastro_jogador)
print('-='*25)

for jogador,valor in cadastro_jogador.items():
    print(f'O campo {jogador} tem o valor {valor[0]}.')
print('-='*25)

print(f'O jogador {cadastro_jogador["nome"][0]} jogou {qntd_partidas} partidas.')
posicao = 1
for valor in cadastro_jogador['gols']:
    for gol in valor:
        print(f'\t=> Na partida {posicao}, fez {gol} gols.')
        posicao += 1
print(f'Foi um total de {cadastro_jogador["total"][0]} gols.')