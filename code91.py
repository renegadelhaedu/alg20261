livros = dict()
op = 99
while op != 0:
    print('1-cadastrar livro')
    print('2-listar livro')
    print('3-atualizar livro')
    print('4-remover livro')
    print('0-sair')
    op = int(input('qual a opcao desejada? '))

    if op == 1:
        isbn = input('qual a isbn do livro? ')
        nome = input('qual o nome do livro? ')
        autor = input('qual o autor do livro? ')
        ano = int(input('qual o ano do livro? '))
        livros[isbn] = {'nome': nome, 'autor': autor, 'ano': ano}
        print('livro cadastrado com sucesso!\n')
    elif op == 2:
        print('\n\n---LISTA DE LIVROS---')
        for chave in livros:
            print(livros[chave]['nome'])

    elif op == 3:
        busca = input('qual o isbn do livro que será atualizado? ')
        if busca in livros:
            novo_nome = input('qual o novo nome do livro? ')
            novo_autor = input('qual o novo autor do livro? ')
            livros[busca]['nome'] = novo_nome
            livros[busca]['autor'] = novo_autor
            print(livros[busca])
            print('livro atualizado com sucesso!\n')
        else:
            print('livro nao encontrado. ISBN inexistente!')

    elif op == 4:
        busca = input('qual o isbn do livro que será removido? ')
        if busca in livros:
            livros.pop(busca)
            print('livro removido com sucesso!\n')
        else:
            print('livro nao encontrado. ISBN inexistente!')


