def notas(*n, sit=False):
    notas_dict = {}
    notas_dict['total'] = len(n)
    notas_dict['maior'] = max(n)
    notas_dict['menor'] = min(n)
    notas_dict['media'] = sum(n) / len(n)
    media = notas_dict['media']
    if sit:
        if media < 6:
            notas_dict['situacao'] = 'RUIM'
        elif media == 6:
            notas_dict['situacao'] = 'RAZOÁVEL'
        else:
            notas_dict['situacao'] = 'BOA'
    return notas_dict

resp = notas(4, 3.3, 5, 10, sit=True)
print(resp)
