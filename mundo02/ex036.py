casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
qntd_anos = float(input('Digite em quantos anos ele vai pagar: '))

prestacao_mensal = casa / (qntd_anos * 12)

if (prestacao_mensal > salario * 0.3):
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
