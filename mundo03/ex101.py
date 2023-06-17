import time
ano_atual = time.localtime().tm_year

ano_nasc = int(input('Em que ano você nasceu? '))
idade = ano_atual - ano_nasc

def voto(idade):
    if idade < 18:
        voto = 'VOTO NEGADO'
    elif idade > 60:
        voto = 'VOTO OPCIONAL'
    else:
        voto = 'VOTO OBRIGATÓRIO'
    return voto

voto = voto(idade)

print(f'Com {idade} anos: {voto}.')