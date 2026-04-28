p = ['a','b','c','d','e','f']
busca = input('informe a pessoa que voce esta buscando')
encontrei = False
for item in p:
    if busca == item:
        encontrei = True
        break
if encontrei:
    print('eu encontrei a pessoa que voce esta buscando')