peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura (m): '))
imc = peso / (altura * altura)

if imc < 18.5: 
    print('Abaixo do Peso')
elif imc < 25: 
    print('Peso ideal')
elif imc < 30: 
    print('Sobrepeso')
elif imc < 40: 
    print('Obesidade')
else:
    print('Obesidade mórbida')
