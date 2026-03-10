#desenvolva um algoritmo em python que leia o nome, idade, salario
# de um jogador de futebol. se ele receber ate 5000, tiver idade 
#maior que 32 e o nome dele for adilson, contrate ele para o atlet cz

nome = input('digite seu nome')
idade = int(input('digite sua idade'))
salario = float(input('digite seu salario'))

if nome == 'adilson' and idade > 32 and salario <= 5000:
    print('pode jogar no atletico')

else:
    print('nao é ruim o suficiente')
