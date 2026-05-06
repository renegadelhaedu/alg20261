a = ['jose','joseana','joaquim','jeferson']
resultado = []
busca  = 'jo'
for item in a:
    if busca in item:
        resultado.append(item)

print(resultado)