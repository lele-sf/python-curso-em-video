import datetime

ano_nasc = int(input('Digite o seu ano de nascimento: '))
ano_atual = datetime.datetime.now().date().year
idade = ano_atual - ano_nasc

if idade < 18:
    print(f'Você ainda vai se alistar.\nFalta {18 - idade} anos para o alistamento.')
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print(f'Já passou o tempo de se alistar.\nSe passou {idade -18} anos do prazo de alistamento.')

