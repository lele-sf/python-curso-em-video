import time

ano_nasc = int(input('Digite o seu ano de nascimento: '))
ano_atual = time.localtime().tm_year
idade = ano_atual - ano_nasc

if idade < 9:
    print('MIRIM')
elif idade < 14:
    print('INFANTIL')
elif idade < 19:
    print('JUNIOR')
elif idade < 20:
    print('SÊNIOR')
else:
    print('MASTER')