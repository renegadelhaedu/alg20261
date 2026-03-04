#desenvolva um algoritmo em python para ler a nota do TCC de um aluno
#do curso de ciência da computaçao. o programa deve ler também se 
#o aluno publicou o TCC em uma revista científica.

nota = float(input('digite sua nota '))
publicou = input('voce publicou em revista? sim ou nao')


if nota >= 7 or publicou == 'sim':
    print('voce esta aprovado')
else:
    print('voce esta reprovado')
    print('voce esta reprovado')