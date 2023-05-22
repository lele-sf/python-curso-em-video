total = 0
mais_mil = 0
prod_barato = ''
preco_barato = float('inf')

while True:
    nome_prod = str(input('Nome do Produto: '))
    preco_prod = float(input('Preço: R$'))
    opcao = ' '
    total += preco_prod

    if preco_prod > 1000:
            mais_mil += 1

    if preco_prod < preco_barato:
        prod_barato = nome_prod
        preco_barato = preco_prod

    while opcao not in 'SN':
        opcao = input('Quer continuar [S/N]? ').upper().strip()[0]

    if opcao == 'S':
        continue
    elif opcao == 'N':
        break

print(f'O total da compra foi R${total:.2f}\nTemos {mais_mil} produtos custando mais de R$1000.00\nO produto mais barato foi {prod_barato} que custa R${preco_barato:.2f}')