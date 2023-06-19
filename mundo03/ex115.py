from utilidades import dados

while True:
    dados.titulo_menu('MENU PRINCIPAL')
    print('1 - Ver pessoas cadastradas\n2 - Cadastrar nova Pessoa\n3 - Sair do Sistema')
    dados.linha(42)
    opcao = dados.leia_opcao('Sua Opção: ')
    if opcao == 1:
        dados.titulo_menu('PESSOAS CADASTRADAS')
        cadastros = dados.carregar_cadastros()
        if not cadastros:
            print('Nenhuma pessoa cadastrada.')
        else:
            for nome, idade in cadastros:
                print(f'{nome:<30} {idade:>3} anos')

    elif opcao == 2:
        dados.titulo_menu('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = dados.leia_idade('Idade: ')
        dados.salvar_cadastro(nome, idade)
        print(f'Novo registro de {nome} adicionado.')

    elif opcao == 3:
        dados.titulo_menu('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')