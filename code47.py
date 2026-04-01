#faça um programa em python que leia a idade
#dos alunos de uma turma de p1. calcule a média
#e mostre o resultado. pare de ler notas quando
#o usuário digitar um valor negativo

idade = 0
soma = 0
qtde = 0
while idade >= 0:
    soma = soma + idade
    idade = int(input('qual sua idade? '))
    qtde = qtde + 1
    
if qtde - 1 > 0:
    media = soma / (qtde - 1)
    print('QTDE: ', qtde)
    print(media)
else:
    print('nenhum usuário digitou idade válida')

