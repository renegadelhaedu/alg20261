sim = 0
nao = 0
nome = ''
while sim < 5 and nome != 'kamile':
    nome = input('qual teu nome? ')
    resposta = input('bora dançar? cuida!')
    if resposta == 'sim':
        sim = sim + 1
    else:
        nao = nao + 1
perc = (sim /(sim + nao)) * 100
print('arthur cajú venceu na vida')
print('mas ele levou alguns nao: ', nao)
print(f'Sua taxa de sucesso foi de {perc:.2f}%')
