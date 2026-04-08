#questao 38 da lista de repetição
salario = float(input('Qual o seu salario?\n'))
ano = 1996
taxa = 0.015
while ano < 2026:
    salario *= 1+taxa
    taxa *= 2
    ano += 1
print(f'Seu salario atual é {salario}')

