#arquivos
#escrita em arquivos com modo:
# w -> sobrescreve tudo que tem dentro do arquivo
# a -> atualiza o que tem dentro do arquivo
# r -> leitura de arquivos
pessoas = []
arquivo = open('farrachico.txt', 'r')

linhas = arquivo.readlines()
arquivo.close()
for linha in linhas:
    for pessoa in linha.split(','):
        pessoas.append(pessoa.replace('\n','').strip())

print(pessoas)

