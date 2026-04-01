#questao 19

numero = int(input('diga um numero'))
if numero < 1000:
    qtde100 = numero // 100
    resto = numero % 100
    qtde10 = resto // 10
    resto = resto % 10
    qtde1 = resto
    print('quantidade de centenas: ', qtde100)
    print('quantidade de dezenas: ', qtde10)
    print('quantidade de unidades: ', qtde1)