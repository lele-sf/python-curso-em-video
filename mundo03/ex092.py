import time
ano_atual = time.localtime().tm_year

cadastro_pessoa = {'nome':[],'idade':[],'ctps':[],'contração':[],'salário':[],'aposentadoria':[]}

while True:
    nome = input('Nome: ')
    cadastro_pessoa['nome'].append(nome)
    ano_nasc = int(input('Ano de nascimento: '))
    idade = ano_atual - ano_nasc
    cadastro_pessoa['idade'].append(idade)
    ctps = int(input('Carteira de Trabalho (0 não tem): '))
    cadastro_pessoa['ctps'].append(ctps)
    if ctps == 0:
        del cadastro_pessoa['contração'], 
        del cadastro_pessoa['salário']
        del cadastro_pessoa['aposentadoria']
        break
    contratacao = int(input('Ano de contratação: '))
    cadastro_pessoa['contração'].append(contratacao)
    salario = float(input('Salário: R$'))
    cadastro_pessoa['salário'].append(salario)
    aposentadoria = (contratacao + 35) - ano_nasc
    cadastro_pessoa['aposentadoria'].append(aposentadoria)
    break

print(cadastro_pessoa)

for pessoa,valor in cadastro_pessoa.items():
    print(f'{pessoa} tem o valor {valor[0]}')