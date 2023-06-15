cadastro_jogador = []

while True:
    jogador = {}

    nome = input('Nome do jogador: ')
    qntd_partidas = int(input(f'Quantas partidas {nome} jogou? '))
    jogador['nome'] = nome

    gols_partidas = []

    for partida in range(qntd_partidas):
        gols = int(input(f'Quantos gols na partida {partida + 1}? '))
        gols_partidas.append(gols)

    jogador['gols'] = gols_partidas

    total_gols = sum(gols_partidas)
    jogador['total'] = total_gols

    cadastro_jogador.append(jogador)

    escolha = input('Quer continuar? [S/N] ').upper()
    if escolha == 'N':
        break

print('-='*25)
print(cadastro_jogador)
print('cod  nome    gols           total')
print('-'*35)
for cod, jogador in enumerate(cadastro_jogador):
    nome = jogador['nome']
    gols = jogador['gols']
    total = jogador['total']
    print(f'{cod:<5}{nome:<8}{gols}{total:>12}')
print('-'*35)

while True:
    dados = int(input('Mostrar dados de qual jogador? '))
    for cod, jogador in enumerate(cadastro_jogador):
        if dados == cod:
            nome = jogador['nome']
            gols = jogador['gols']
            total = jogador['total']
            print(f'-- LEVANTAMENTO DO JOGADOR {nome}:')
            for partida, gol in enumerate(gols):
                print(f'No jogo {partida+1} fez {gol} gols.')
            break
    opcao = input('Deseja continuar? [S/N] ').upper()
    if opcao == 'N':
        break