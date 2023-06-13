tupla_0a20 = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
                'doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    num = int(input('Digite um número de 0 a 20: '))
    
    if num < 0 or num > 20:
        print('Tente novamente. ',end='')
        continue

    palavra = tupla_0a20[num]

    print(f'O número digitado foi {palavra}.')
    break