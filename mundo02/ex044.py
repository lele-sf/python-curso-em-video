preco_normal = float(input('Digite o preço do produto: R$'))
cond_pag = int(input('Escolha a forma de pagamento:\n1- À vista dinheiro/cheque\n2- À vista no cartão\n3- até 2x no cartão\n4- 3x ou mais no cartão\nOpção: '))
desconto_10 = preco_normal - (preco_normal * 0.1)
desconto_5 = preco_normal - (preco_normal * 0.05)
juros_20 = preco_normal + (preco_normal * 1.20)

match cond_pag:
    case 1:
        print(f'Valor do produto: R${desconto_10:.2f}')
    case 2:
        print(f'Valor do produto: R${desconto_5:.2f}')
    case 3:
        print(f'Valor do produto: R${preco_normal:.2f}')
    case 4:
        print(f'Valor do produto: R${juros_20:.2f}')
    case _:
        print('Opção inválida!')