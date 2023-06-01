tupla = []

for i in range(4):
    num = int(input('Digite um número: '))
    tupla.append(num)

qntd_nove = tupla.count(9)

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {qntd_nove} vezes')

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram ',end='')
for n in tupla:
    if n % 2 == 0:
        print(n,end=' ')