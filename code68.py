num = 2.3445346
contagem = 0
achei = False
for c in str(num):
    if c == '.':
        achei = True
        continue
    if achei == True:
        contagem = contagem + 1

print(contagem)