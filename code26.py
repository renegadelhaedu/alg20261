#questao 11
salario = float(input('digite seu salario '))
if salario <= 280:
    percentual = 0.2
if salario > 280 and salario <= 700:
    percentual = 0.15
if salario > 700 and salario <= 1500:
    percentual = 0.1
if salario > 1500:
    percentual = 0.05

print(f'seu salario era {salario}')
print(f'voce recebeu aumento de {percentual * 100} %')
aumento = salario * percentual
print(f'voce tera um aumento de {aumento} reais')
final = salario + aumento
print(f'seu salario final será {final} reais')