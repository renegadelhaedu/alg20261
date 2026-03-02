#construa um algoritmo que calcule e exiba a velocidade média de um carro que sairá de Sousa até cajazeiras e leva apenas 30 minutos. o desenvolvedor deve inserir os valores no programa. 
#neste exemplo, o usuário deve inserir os 2 valores

distancia = float(input('digite o valor da distância percorrida em kms '))
tempo = float(input('digite o valor do tempo em minutos '))
tempo = tempo / 60
vm = distancia / tempo
print('a velocidade media do usuario foi', vm)