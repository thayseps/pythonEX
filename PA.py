print(' ')
print('10 PRIMEIROS TERMOS DE UMA P.A.')
print(' ')
pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
dec = pt + (10 - 1) * razao
for c in range(pt, dec + razao, razao):
    print('{} '.format(c), end='-> ')

print('fim')
