nomes = [['maria clara','sousa'],['matheus','vieiropolis'],['maria rita','cajazeiras']]

busca = input('digite o nome da pessoa')
retorno = []
for p in nomes:
    if busca in p[0]:
        retorno.append(p)

print(retorno)