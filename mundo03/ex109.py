from utilidades import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.format(p, True)} é {moeda.format(moeda.metade(p), True)}')
print(f'O dobro de {moeda.format(p,False)} é {moeda.format(moeda.dobro(p),True)}')
print(f'Aumentando 10%, temos {moeda.format(moeda.aumentar(p, 10),True)}')
print(f'Reduzindo 13%, temos {moeda.format(moeda.diminuir(p, 13),True)}')
