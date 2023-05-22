primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))    
termo = primeiro_termo
cont = 1
total = 0
mais_termo = 10

while mais_termo != 0:
    total += mais_termo
    while cont <= total:
        print(f'{termo} → ',end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais_termo = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')