import random

num_aleatorio = random.randint(1,5)
num_usuario = int(input('Adivinhe qual é o número(1 a 5): '))

if num_usuario == num_aleatorio:
    print('Parabéns! Você acertou!')
else:
    print('Errou! Tente novamente.')