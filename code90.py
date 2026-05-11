profs = {'rene':['algoritmos', 'inteligencia artificial'] , 'luciano':['poo', 'eng soft 1'],'ludgero':['redes']}

#traz o valor conforme a chave fornecida
#print(profs.get('ludgero'))

professor = input('qual o professor? ')
removida = input('qual o nome da disciplina para remover? ')

profs[professor].remove(removida)

print(profs)