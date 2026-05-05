adms = []
clientes = []

op = -99
while op != 0:
    print('menu')
    print('1 - cadastrar adm')
    print('2 - cadastrar cliente')
    print('3 - login')

    op = int(input())
    if op == 1:
        nome = input()
        login = input()
        senha = input()
        adms.append([nome, login, senha])

    elif op == 3:
        login = input('diga o login')
        senha = input('diga a senha')
        achei = False
        for a in adms:
            #tem que bater com o cadastrar
            if login == a[0] and senha == a[2]:
                achei = True
                break

