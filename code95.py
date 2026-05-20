#funções com retorno
def calcular_nota(n1, n2, n3, comportamento):
    media = (n1 + n2 + n3) / 3
    if comportamento == "bom":
        media = media * 1.15
    elif comportamento == "errado":
        media = media * 0.9

    return media

rikkellmy = calcular_nota(5,7,7,'bom')
c__o = calcular_nota(7,7,7,'errado')
print(rikkellmy)
print(c__o)

