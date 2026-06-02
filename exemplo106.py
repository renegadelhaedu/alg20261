dic = {'a':'maria', 'b':'joao','c':'josemaria'}

nome = input('Qual o nome?')
arquivo = open(nome + '.txt', 'w')

for chave,valor in dic.items():
    arquivo.write(valor+'\n')

arquivo.close()