lado1 = int(input('Digite o comprimento do primeiro lado: '))
lado2 = int(input('Digite o comprimento do segundo lado: '))
lado3 = int(input('Digite o comprimento do terceiro lado: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print('É possível formar um triângulo com esses lados.')

    if lado1 == lado2 == lado3:
        print('E é um triângulo Equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('E é um triângulo Isósceles')
    else:
        print('E é um triângulo Escaleno')

else:
    print('Não é possível formar um triângulo com esses lados.')
