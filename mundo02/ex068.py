from random import randint

def par(num):
    return num % 2 == 0
def impar(num):
    return num % 2 == 1
total_vitorias = 0

while True:
    player = int(input('Digite um número: '))
    random_number = randint(0,10)
    soma = player + random_number
    par_impar = ' '

    while par_impar not in 'PI':
        par_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {player} e o computador {random_number}. Total de {soma} ', end='')
    print('DEU PAR' if par(soma) else 'DEU ÍMPAR')
    if par_impar == 'P':
        if par(soma):
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    elif par_impar == 'I':
        if impar(soma):
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    total_vitorias += 1
print(f'GAME OVER! Você venceu {total_vitorias} vezes.')