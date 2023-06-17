import pydoc

def linha(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

def help_py():
    comando = input('Função ou Biblioteca > ')
    linha(f'Acessando o manual do comando "{comando}"')

    try:
        pydoc.help(comando)
    except Exception as e:
        print(f'Erro ao exibir o manual do comando: {e}')

linha('SISTEMA DE AJUDA PyHELP')
help_py()
