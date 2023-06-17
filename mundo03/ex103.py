def ficha(nome='', gols=0):
    nome = input('Nome do Jogador: ')
    gols_str = input('Número de Gols: ')

    if gols_str != '':
        gols = int(gols_str)
    else:
        gols = 0

    if nome == '':
        nome = '<desconhecido>'
    
    return nome, gols

nome, gols = ficha()

print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')