idade = int(input('qual sua idade? '))
dinheiro = float(input('quanto de dinheiro voce possui? '))
genero = input('qual seu genero? ')

#operador lógico and  e lógico

if idade >= 18 and dinheiro >= 50 and genero == 'feminino':
    print('pode entrar na boate')
else:
    print('nao pode entrar')