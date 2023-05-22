import random

jokenpo = ["pedra", "papel", "tesoura"]
comp_choice = random.choice(jokenpo)
user_choice = input('Pedra, papel ou tesoura? ').lower()
print(f'Computador: {comp_choice}')

if user_choice == 'pedra' and comp_choice == 'papel' or user_choice == 'papel' and comp_choice == 'tesoura' or user_choice == 'tesoura' and comp_choice == 'pedra':
    print('Você perdeu!')
elif user_choice == comp_choice:
    print('Empate!')
else:
    print('Você ganhou!')