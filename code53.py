#questao 4 - lista de estrutura de repetição

popA = 80000
popB = 200000
txA = 0.03
txB = 0.015
anos = 0

while popA < popB:
    popA = popA * (1 + txA)
    popB = popB * (1 + txB)
    anos = anos + 1

print('a qtde de anos que A igualou ou supe B foi', anos)
