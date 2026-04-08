#break é um comando utilizado para encerrar laços de repet
pessoas = 0
nome = 'qualdasda'
while nome != 'fim':
    nome = input('digite seu nome').lower()
    if nome == 'neymar':
        break
    pessoas += 1

print('qtde:', pessoas)
print('voce digitou neymar e ele é tao ruim que quebrou' \
'o código')
    
