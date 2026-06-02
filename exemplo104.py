#arquivos

#escrita em arquivos com modo:
# w -> sobrescreve tudo que tem dentro do arquivo
# a -> atualiza o que tem dentro do arquivo

nome_arquivo = input('qual o nome do arquivo? ')
#abrindo em modo escrita
arquivo = open(nome_arquivo + '.txt', 'a')

texto = input('Quem foram os convidados da farra de chico? ')
arquivo.write('\n' + texto) #populando o arquivo com texto

#encerrando a conexao com o arquivo
arquivo.close()
