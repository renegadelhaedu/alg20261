#atualizar um item
p = ['a','b','c','d','e','f']

index = -1
busca = input('informe a pessoa que voce esta buscando')
for i in range(len(p)):
    if busca == p[i]:
        index = i
        break
if index >= 0:
    novo_valor = input('qual a boa? ')
    p[index] = novo_valor
    print('elemento atualizado com sucesso')
else:
    print('nao foi possivel encontrar este elemento')





