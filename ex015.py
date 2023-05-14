diaAlugado = int(input('Quantos dias alugados? '))
kmRodado = float(input('Quantos Km rodados? '))

precoTotal = ((60*diaAlugado) + (0.15*kmRodado))

print(f'O total a pagar é de R${precoTotal:.2f}')