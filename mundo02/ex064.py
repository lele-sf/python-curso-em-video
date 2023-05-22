soma = 0
cont = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        cont += 1
        soma += num
        continue
    else:
        break
print(f'Você digitou {cont} números.\nA soma total dos números é {soma}.')