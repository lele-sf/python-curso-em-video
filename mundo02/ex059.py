def obter_numeros():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    return num1, num2

def calcular_operacoes(num1, num2):
    soma = num1 + num2
    multiplica = num1 * num2
    maior = max(num1, num2)
    return soma, multiplica, maior

num1, num2 = obter_numeros()
soma, multiplica, maior = calcular_operacoes(num1, num2)

while True:
    menu_choice = input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nOpção: ')

    if menu_choice == '1':
        print(f'Soma: {soma:.2f}')
        break
    elif menu_choice == '2':
        print(f'Multiplicação: {multiplica:.2f}')
        break
    elif menu_choice == '3':
        print(f'Maior número: {maior:.2f}')
        break
    elif menu_choice == '4':
        num1, num2 = obter_numeros()
        soma, multiplica, maior = calcular_operacoes(num1, num2)
    elif menu_choice == '5':
        break
    else:
        print('Opção inválida. Tente novamente.')