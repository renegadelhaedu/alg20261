ps = []
rene = ['rene',37,70]
rodrigo = ['rodrigo',20,65]
mc = ['maria clara',18,50]
lara = ['Lara',19,64]
ps.append(rene)
ps.append(rodrigo)
ps.append(mc)
ps.append(lara)
soma = 0
for p in ps:
    soma += p[2]
media = soma / len(ps)
print(media)
