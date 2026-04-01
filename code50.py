#crédito 

valor = float(input('tu quer quanto? '))
meses = 0
while meses < 12:
    #valor = (valor * 0.18) + valor
    valor = valor * 1.18
    meses = meses + 1

print('o valor final foi ', valor)
