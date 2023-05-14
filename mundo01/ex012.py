precoProduto = float(input('Digite o preço do produto: R$'))
desconto = precoProduto *0.05
precoDesconto = precoProduto - desconto
print(f'R${precoProduto} + 5% = R${precoDesconto}')