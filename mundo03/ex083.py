expressao = input('Digite uma expressão: ')

contador = 0

for char in expressao:
    if char == '(':
        contador += 1
    elif char == ')':
        contador -= 1
    if contador < 0:
        break

if contador == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
