import random

num_aleatorio = random.randint(1,10)

while True:
    num_usuario = int(input('Adivinhe qual é o número(1 a 10): '))
    if num_usuario == num_aleatorio:
        print('Parabéns! Você acertou!')
        break
    else:
        print('Errou! Tente novamente.')
        continue
