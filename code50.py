#faça um algoritmo em python que leia o nome e
#as duas notas de cada aluno da turma(28 alunos)
#informe ao final a média da turma e o nome
#do aluno com maior média da turma

maior_media = 0
nome_maior = 'maria'
qtde = 0
soma = 0
while qtde < 28:
    nome = input('qual seu nome? ')
    nota1 = float(input('diga a nota '))
    nota2 = float(input('diga a nota '))
    media = (nota1 + nota2) / 2
    if media > maior_media:
        maior_media = media
        nome_maior = nome

    soma = soma + media
    qtde = qtde + 1

mm = soma / qtde
print(mm)
print(nome_maior)
print(maior_media)
