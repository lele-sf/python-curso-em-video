vel_carro = int(input('Digite a velocidade do carro (Km): '))
multa = (vel_carro - 80) * 7

if vel_carro > 80:
    print(f'Você foi multado por ultrapassar o limite de velocidade!\nValor da multa: R${multa}')
