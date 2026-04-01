#faça um programa em python que leia a idade
#dos alunos de uma turma de p1. calcule a soma
#e mostre o resultado. pare de ler notas quando
#o usuário digitar um valor negativo

idade = 0
soma = 0
while idade >= 0:
    soma = soma + idade
    idade = int(input('qual sua idade? '))
    

print(soma)

