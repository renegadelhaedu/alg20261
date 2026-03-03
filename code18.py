curso = input('qual seu curso? ')

if curso == 'computacao':
    resposta = input('qual seu game preferido? ')
else:
    if curso == 'educacao fisica':
        resposta = input('qual o esporte preferido? ')
    else:
        if curso == 'direito':
            resposta = input('voce está usando paletó? ')
        else: 
            resposta = 'essa pessoa nao pertence a nenhum destes cursos'

print(f'esta pessoa cursa {curso} e sua resposta foi {resposta}')
