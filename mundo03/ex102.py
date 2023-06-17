def fatorial(num, show=False):
    fact = 1
    expressao = ''
    for i in range(1, num + 1):
        fact *= i
        if show:
            expressao += f'{i} x '
    if show:
        expressao = expressao[:-3] + f' = {fact}'
        print(expressao)
    else:
        print(f'{num}! = {fact}')
    return fact

fatorial(5, show=True)
fatorial(12)
fatorial(4, show=False)
