#imc
massa = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = massa / (altura ** 2)
print('O seu IMC é de {:.1f}.'.format(imc))
if imc <= 18.5:
    print('Cuidado! Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Cuidado! Você está em sobrepeso.')
elif imc < 40:
    print('Cuidado! Você está obeso.')
elif imc > 40:
    print('Cuidado! Você está com obesidade mórbida.')

