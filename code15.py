#desenvolva um algoritmo em python que leia a altura e o peso 
#calcule o IMC e informe para o usuário qual a categoria

altura = float(input('digite sua altura '))
peso = float(input('digite sua peso '))

imc = peso / (altura * altura)

if imc < 25:
    print('seu imc está normal')

if imc > 30:
    print('voce está obeso')

if imc >= 25:
    print('voce está com sobrepeso')
#para pensar 


