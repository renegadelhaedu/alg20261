#operadores lógicos
#negação lógica   not
resposta = input('voce esta conectado a internet?')
if resposta == 'sim':
    status = True
else:
    status = False

if not status:
    print('mensagem')