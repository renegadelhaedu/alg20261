#questao 14 lista de est de decisao

n1 = float(input('digite sua primeira nota'))
n2 = float(input('digite sua segunda nota'))

media = (n1 + n2) / 2
if media < 0 or media > 10:
    print('notas invalidas')
else:
    if media >= 9 and media <= 10:
        print('A')
    elif media >= 7.5 and media < 9:
        print('B')
    elif media >= 6 and media < 7.5:
        print('C')
    elif media >= 4 and media < 6:
        print('D')
    elif media >= 0 and media < 4:
        print('E')

