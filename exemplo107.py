#list comprehension
inicial = [1,2,3,4,5,6,7,8]
final = [x*2 for x in inicial if x % 2 == 0]
#print(final)

nomes = ['arthur','chico','felipe','maria clara','kamille']
maisc = [nome.upper() for nome in nomes if 'a' in nome]
#print(maisc)

par = {nome: len(nome) for nome in nomes}
print(par)