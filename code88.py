profs = {'rene':['algoritmos', 'inteligencia artificial'] , 'luciano':['poo', 'eng soft 1'],'ludgero':['redes']}

#professor = input('qual o professor? ')
#nova_disciplina = input('qual o nova disciplina? ')

#profs[professor].append(nova_disciplina)

print(profs)

#removendo o par chave:valor
abandonao = input('qual o nome do professor que decidiu nos deixar? ')
profs.pop(abandonao) #elimina a dupla chave:valor
print(profs)