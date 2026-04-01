caim1 = float(input('diga uma nota'))
caim2 = float(input('diga uma nota'))
abel1 = float(input('diga uma nota'))
abel2 = float(input('diga uma nota'))

media_caim = (caim1 + caim2) / 2
media_abel = (abel1 + abel2) / 2

if media_caim >= 7:
    print('caim está aprovado')
elif media_caim >= 5:
    print('caim está na recuperação')
else:
    print('caim está reprovado')


if media_abel >= 7:
    print('caim está aprovado')
elif media_abel >= 5:
    print('caim está na recuperação')
else:
    print('caim está reprovado')

if media_caim > media_abel:
    print('caim tirou nota maior que abel')
elif media_abel > media_caim:
    print('abel tirou nota maior que caim')
else:
    print('as médias sao iguais')