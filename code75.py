#remover um item
p = ['a','b','c','d','e','f']

index = -1
busca = input('informe a pessoa que voce esta buscando')
for i in range(len(p)):
    if busca == p[i]:
        index = i
        break
if index >= 0:
    p.pop(index)
    print('elemento eliminado com sucesso')
else:
    print('nao foi possivel encontrar este elemento')