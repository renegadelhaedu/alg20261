
nova_lista = list()
p = [['rene',37],['carlos',17],['gabriel',18]]
index = -1
for i  in range(len(p)):
    if p[i][1] == 'jose':
        index = i
nova_lista.append(p[index])
p.pop(index)


