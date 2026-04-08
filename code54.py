#poupança - 1.1% e é uma aplicação isenta
#tesouro ipca+ 2028 - 1.3% - tributa 15% do lucro

valor_inicial = float(input('qual o valor? '))
aplic_a = valor_inicial
aplic_b = valor_inicial
mes = 1
while mes <= 24:
    aplic_a = aplic_a * 1.011
    aplic_b = aplic_b * 1.013
    mes = mes + 1

imposto_b = (aplic_b - valor_inicial) * 0.15
liq_b = aplic_b - imposto_b

if liq_b > aplic_a:
    print('B rendeu mais:', liq_b - aplic_a)
else:
    print('A rendeu mais:', aplic_a - liq_b)

print(f'A rendeu {aplic_a} e B rendeu {liq_b}')