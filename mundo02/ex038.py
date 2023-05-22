num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 > num2:
    print(f'O primeiro valor "{num1}" é o maior')
elif num2 > num1:
    print(f'O segundo valor "{num2}" é o maior')
else:
    print('Os valores são iguais')