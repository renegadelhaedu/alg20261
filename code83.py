a = ['rara','zeze','didi','popo','tata','nenem']
busca = 'popo fazer input'
achei = -1
for i in range(len(a)):
    if busca == a[i]:
        achei = i
if achei >= 0:
    a.pop(achei)
    print('removi com sucesso')
else:
    print('nao ta na lista')


