def leiaInt(n):
    while True:
        num = input(n)
        if num == '':
            print('Usuário preferiu não digitar esse número.')
            return 0
        try:
            return int(num)
        except ValueError:
            print(f'ERRO! "{num}" não é um número inteiro válido.')

def leiaFloat(n):
    while True:
        num = input(n)
        if num == '':
            print('Usuário preferiu não digitar esse número.')
            return 0
        try:
            return float(num)
        except ValueError:
            print(f'ERRO! "{num}" não é um número real válido.')

def leia_opcao(mensagem):
    while True:
        opcao = input(mensagem)
        if not opcao.strip():
            print('ERRO! Digite uma opção válida!')
        else:
            try:
                opcao_int = int(opcao)
                return opcao_int
            except ValueError:
                print('ERRO! Digite uma opção válida!')

def leia_idade(n):
    while True:
        num = input(n)
        try:
            return int(num)
        except ValueError:
            print(f'ERRO! "{num}" não é um número inteiro válido.')

def titulo_menu(msg):
    linha = '-' * 42
    txt_center = msg.center(42)
    
    print(linha)
    print(txt_center)
    print(linha)

def linha(tam):
    linha = '-' * tam
    print(linha)

def salvar_cadastro(nome, idade):
    with open('cadastros.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome},{idade}\n')


def carregar_cadastros():
    cadastros = []
    try:
        with open('cadastros.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome, idade = linha.strip().split(',')
                cadastros.append((nome, int(idade)))
    except FileNotFoundError:
        return cadastros
    return cadastros