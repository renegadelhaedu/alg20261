#comando para adicionar no seu arquivo python o pacote random
import random
meses = int(input('quantos meses de salário? '))
salario = float(input('qual teu salário? '))
soma = 0

for mes in range(meses):
    #gerando número inteiros aleatórios entre 1 e 5
    tx = random.randint(1,5)
    sal_aumentado = salario * (1 + tx/100)
    soma = soma + sal_aumentado
    

print(f'ao longo de {meses} meses, você recebeu {soma}')

