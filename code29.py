#questao 16

a = int(input('digite '))
b = int(input('digite '))
c = int(input('digite '))

if a == 0:
    print('nao é equacao do segundo grau')
else:
    delta = b ** 2 - 4 * a * c 
    if delta < 0:
        print('nao tem raizes')
    if delta == 0:
        x1 = (-b + delta ** (1/2)) / (2*a)
        print(f'o valor da raiz real é {x1}')
    if delta > 0:
        x1 = (-b + delta ** (1/2)) / (2*a)
        x2 = (-b - delta ** (1/2)) / (2*a)
        print(f'o valor x1  é {x1} e de x2 é {x2}')
        