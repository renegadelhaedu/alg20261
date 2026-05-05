#construa um algoritmo em python que cria uma lista vazia pessoas
#o algoritmo deve ir lendo o nome e a idade de cada usuário (6),
#compondo eles numa lista e inserindo em pessoas


p = []

for i in range(2):
    nome = input('qual seu nome ')
    idade = int(input('qual sua idade '))
    p.append([nome,idade])

for pessoa in p:
    if pessoa[1] >= 18:
        print('Nome:',pessoa[0],' | idade:',pessoa[1])


