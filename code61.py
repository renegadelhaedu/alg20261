nome = ''
perdeu = False 
while nome != 'caderno':
    le = input('informe uma letra: ')
    if le == 'k' or le == 'y' or le == 'w':
        continue
    nome = nome + le
    print('a palavra em formaçao é: ',nome)
    if len(nome) == 7 and nome != 'caderno':
        print('voce perdeu')
        perdeu = True
        break
    
if not perdeu:
    print('voce ganhou')
    