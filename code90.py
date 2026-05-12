profs = {'rene':['algoritmos', 'inteligencia artificial'] , 'luciano':['poo', 'eng soft 1'],'ludgero':['redes']}

#for chave, valor in profs.items():
#    print(chave, valor)

#traz o valor conforme a chave fornecida
#print(profs.get('ludgero'))

#professor = input('qual o professor? ')
#removida = input('qual o nome da disciplina para remover? ')

#profs[professor].remove(removida)

#print(profs)

#for com todos os valores
for valor in profs.values():
    print(valor)

#deveria: só acessar o valor se tiver a respectiva chave (em python não é assim)

