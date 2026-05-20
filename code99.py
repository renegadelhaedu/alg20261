import code97
import code98
usuarios = [['rene','rnsg','123'],['eric','ed','amigoderodrigo']]

op = 99
while op != 0:
    op = code97.menu()
    if op == 1:
        login = input('Login: ')
        senha = input('Senha: ')
        logado = code98.verificar_login(login, senha, usuarios)
        if logado:
            print('Login feito com sucesso')
            print('mostrar menu de usuario logado')
        else:
            print('Login incorreto')

    if op == 4:
        print('deletar todos os usuarios')
        code98.limpar_lista(usuarios)
        print(usuarios)