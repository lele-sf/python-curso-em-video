n = int(input("Digite o número de termos da sequência Fibonacci: "))
fibonacci = [0, 1]

while len(fibonacci) < n: 
    # 2 < n(termo)  ex: 2 < 5 
    prox_termo = fibonacci[-1] + fibonacci[-2] 
    # ultimo_termo + penultimo_termo  ex: 0 1 1 2 3
    fibonacci.append(prox_termo) # ex: [0,1,1,2,3] - len = 5
                                    
print('Início ',end='')
for termo in fibonacci:
    print(f'→ {termo}', end=" ")
