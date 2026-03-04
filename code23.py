#questao 15 lista de decisao
l1 = int(input('digite o lado'))
l2 = int(input('digite o lado'))
l3 = int(input('digite o lado'))

if l1 == l2 and l2 == l3:
    print('equilatero')
else:
    if l1 != l2 and l2 != l3 and l1 != l3:
        print('escaleno')
    else:
        if (l1 == l2 and l2 != l3) or (l1 == l3 and l3 != l2) or (l2 == l3 and l3 != l1):
            print('isosceles')            