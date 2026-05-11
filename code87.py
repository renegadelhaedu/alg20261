#dicionário (mapa) dict
#estrutura de dados
#par chave:valor
#chave não pode ser uma estrutura de dados
#chaves são únicas
#deve-se controlar a alteração dos valores via chave
#valor pode ser qualquer coisa, float, int, string, boolean, outras estruturas de dados

a = list()
b = set()
c = dict()

lista = ['1','2','3','4','5','6','7','8','9']
set = {'rene','casa','teste'}

#inicializado preenchido
meu_dici = {'rene':3424 , 'rodrigo': 7231 , 'maria aline' : 9876}
#inicializado vazio
dici = dict()

#atribuindo valores ao dicionário (par chave:valor)
#nome_dicionario[chave] = valor
dici['rene'] = 1.70
dici['rodrigo'] = 1.73
#capturando o valor mediante a sua chave
#print(dici['rene'])

#alterando valor do dicionário
competidores = {1:'higor', 2:'rene', 3:'kamille', 4:'eric'}

competidores[2] = 'arthur'
#print(competidores)

#verifica se o item está dentro das chaves deste dicionário
#print('higor' in competidores)

for chave in competidores:
    if competidores[chave] == 'joao vitor':
        print('achei o homi')

for valor in competidores.values():
    if valor == 'joao victor':
        print('achei o homi')



