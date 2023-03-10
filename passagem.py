from time import sleep
d = float(input('Qual a distância da sua viagem?'))
print('Você estáprestes a iniciar uma viagem de {}Km'.format(d))
print('Calculando rota...')
sleep(2)
if d <= 200:
    d1 = d * 0.5
    print('O preço da sua passagem total é R${:.2f}'.format(d1))
else:
    d2 = d * 0.45
    print('O preço da sua passagem é R${:.2f}'.format(d2))
