#desenvolva um algoritmo em python que leia a altura e o peso 
#calcule o IMC e informe para o usuário qual a categoria

altura = float(input('digite sua altura '))
peso = float(input('digite sua peso '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('voce esta com baixo imc')
else:
    if imc < 25:
        print('seu imc está normal')
    else:
        if imc < 30:
            print('voce está com sobrepeso')
        else:
            #if imc >= 30: nao é errado porém aumenta um teste
            print('voce está obeso')



