#fatiando numerossssssss
from time import sleep
num = int(input('\033[7;40mInforme um número:\033[m '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[36m-=\033[m'*20)
print('\033[7;40mAnalisando número {}{}{}\033[m'.format('\033[4m', num, '\033[m'))
print('\033[36m-=\033[m'*20)
sleep(2)
print('Unidade: \033[36m{}\033[m'.format(u))
print('Dezena: \033[35m{}\033[m'.format(d))
print('Centena: \033[34m{}\033[m'.format(c))
print('Milhar: \033[32m{}\033[m'.format(m))
