salario = float(input('Digite o seu salário: '))

if salario > 1250:
    sal_aumento = salario * 1.10
    print(f'Seu novo salário é R${sal_aumento:.2f}')
else:
    sal_aumento = salario * 1.15
    print(f'Seu novo salário é R${sal_aumento:.2f}')