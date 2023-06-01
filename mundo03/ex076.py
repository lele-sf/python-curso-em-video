produtos = [
    {'nome':'Lápis','preco':1.75},{'nome':'Borracha','preco':2.00},{'nome':'Caderno','preco':15.90},{'nome':'Estojo','preco':25.00},
    {'nome':'Transferidor','preco':4.20},{'nome':'Compasso','preco':9.99},{'nome':'Mochila','preco':120.32},{'nome':'Canetas','preco':22.30},{'nome':'Livro','preco':34.90},
]
print(f'{"-"*35}\n\tLISTAGEM DE PREÇOS\n{"-"*35}')

for item in produtos:
    print(f"{item['nome']:.<30} R${item['preco']:>7.2f}")

print(f'{"-"*35}')