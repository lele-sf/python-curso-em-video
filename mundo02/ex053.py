frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
sem_espaco = ''.join(palavras)
inverso = ''

for letra in range(len(sem_espaco) - 1,-1,-1):
    inverso += sem_espaco[letra]
print(f'O inverso de {frase} é {inverso}')
if inverso == sem_espaco:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')