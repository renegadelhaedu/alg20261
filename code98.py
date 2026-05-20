nome_completo = 'alex'
def verificar_login(login:str, senha:str, lista:list):
    for usuario in lista:
        if usuario[1] == login and usuario[2] == senha:
            return True
    return False

def limpar_lista(lista):
    lista.clear()

alunos = []

def mudar_nome():
    global nome_completo
    nome_completo = 'jose'

def aumentar_alunos():
    alunos.append('rene e maria')

mudar_nome()
print(nome_completo)

