def metade(num):
    num /= 2
    return num

def dobro(num):
    num *= 2
    return num

def aumentar(num, porcento):
    p = num * (porcento / 100)
    valor_aumentado = num + p
    return valor_aumentado

def diminuir(num,porcento):
    p = num * (porcento / 100)
    valor_diminuido = num - p
    return valor_diminuido

def format(n,show=False):
    if show == True:
        return f'R${float(n):.2f}'.replace('.', ',')
    else:
        return n

def titulo(msg):
    tam = len(msg) * 2
    print('-'*tam)
    print(f'\t{msg}')
    print('-'*tam)

def leiaNum(n):
    while True:
        num = input(n)
        num = num.replace(',', '.')
        try:
            return float(num)
        except ValueError:
            if num == '':
                print('ERRO! Nenhum valor foi inserido.')
            else:
                print(f'ERRO! "{num}" não é um número válido.')


def resumo(num,aumento,reducao):
    titulo('RESUMO DO VALOR')
    print(f'Preço analisado: \t{format(num,True)}')
    print(f'Dobro do preço: \t{format(dobro(num),True)}')
    print(f'Metade do preço: \t{format(metade(num),True)}')
    print(f'{aumento}% de aumento: \t{format(aumentar(num,aumento),True)}')
    print(f'{reducao}% de redução: \t{format(diminuir(num,reducao),True)}')
    print('-'*31)