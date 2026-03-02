#desenvolva um algoritmo em python que leia a altura e o peso 
#calcule o IMC e informe para o usuário se ele tá obeso ou nao

altura = float(input('digite sua altura '))
peso = float(input('digite sua peso '))

imc = peso / (altura * altura)

if imc > 30:
    print('procure se cuidar pois sua saúde está em risco')
else:
    print('nao está obeso')