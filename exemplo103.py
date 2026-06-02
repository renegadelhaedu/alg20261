#arquivos

#escrita em arquivos com modo:
# w -> sobrescreve tudo que tem dentro do arquivo

#abrindo em modo escrita
arquivo = open('farrachico.txt', 'w')

texto = input('Quem foram os convidados da farra de chico? ')
arquivo.write(texto) #populando o arquivo com texto

#encerrando a conexao com o arquivo
arquivo.close()
