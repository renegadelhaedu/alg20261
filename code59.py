op = 99
while op != 0:
    print('----MENU----')
    print('1-ler nome, idade e estado civil')
    print('2-calcular IMC')
    print('0-sair')
    op = int(input('digite a opcao: '))
    if op == 1:
        nome = input('qual teu nome? ')
        idade = int(input('qual sua idade? '))
        estcv = input('voce é solteiro? ').lower()
        if idade >= 40 and estcv == 'sim':
            print('deu ruim. casa mais nao')
    
    elif op == 2:
        peso = float(input('qual teu peso? '))
        altura = float(input('qual sua altura? '))

        imc = peso / (altura ** 2)
        print(f'Seu IMC é {imc}')
    