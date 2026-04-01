#a faculdade católica pediu para rodrigo desenvolver um 
#sistema que faça a leitura do horário, da distancia percorrida
#pelo aluno até chegar na faculdade e do curso do aluno.
#o sistema deve aceitar a entrada de alunos seguindo a regra:
#gastou até 30km, deixe entrar até 19h
#gastou até 60km, deixe entrar até 19:20
#gastou até 100km, deixe entrar até 19:30
#gastou mais de 100km, deixe entrar até 19:50
#se o aluno for de computaçao deixe entrar qualquer hora

horas = int(input('diga a hora que voce chegou'))
min = int(input('diga o minuto que voce chegou'))
curso = input('qual o curso - cc, dir, ef, fil')
dist = float(input('digite a distancia'))

if dist <= 30 and (horas == 19 and min == 0) or horas == 18:
    print('pode entrar')
elif dist <= 60 and (horas == 19 and min <= 20) or horas == 18:
    print('pode entrar')
elif dist <= 100 and (horas == 19 and min <= 30) or horas == 18:
    print('pode entrar')
elif dist > 100 and (horas == 19 and min <= 50) or horas == 18:
    print('pode entrar')
elif curso == 'cc':
    print('pode entrar')
else:
    print('NAO pode entrar hoje. chegue mais cedo')