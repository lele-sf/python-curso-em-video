num = int(input("Digite um número entre 0 e 9999: "))

milhar = num // 1000
centena = (num % 1000) // 100
dezena = (num % 100) // 10
unidade = num % 10

print(f"O número {num} é formado por: \nMilhar: {milhar}\nCentena: {centena}\nDezena: {dezena}\nUnidade: {unidade}")
