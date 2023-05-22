num = int(input('Digite um número: '))
conversao = int(input('Escolha uma das opções:\n1- Binário\n2- Octal\n3- Hexadecimal\nOpção: '))

match conversao:
    case 1:
        binario = format(num,'b')
        print(f'Binário: {binario}')
    case 2:
        octal = format(num,'o')
        print(f'Octal: {octal}')
    case 3:
        hexadecimal = format(num,'x')
        print(f'Hexadecimal: {hexadecimal}')
    case _:
        print('Opção inválida!')
