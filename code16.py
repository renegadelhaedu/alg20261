n1 = float(input('digite a sua primeira nota '))
n2 = float(input('digite a sua segunda nota '))
n3 = float(input('digite a sua terceira nota '))

media = (n1 + n2 + n3) / 3

if media >= 7:
    print('voce foi aprovado direto')

else:
    print('voce vai para a final')
    nota_final = float(input('qual foi a nota da final? '))

    if nota_final >= 7:
        print('voce foi aprovado. uhuuuu')
    else:
        print('voce vai repetir a disciplina e conseguirá passar')