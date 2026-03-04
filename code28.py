#sabendo que o salario do colaborador é calculado na regra:
#se ele recebe mais de 4 salario minimo, deve descontar apenar 5%
#se ele recebe menos de 4 salarios mninimos, nao desconte nada e bonifique o salario em 7,5%
#faça um programa que leia o salario e exiba na tela o salario final

salario = float(input('digite seu salario'))
sm = 1621

if salario > 4 * sm:
    final = salario * 0.95 #retirando 5%
else:
    final = salario * 1.075 #aumentando 7,5%