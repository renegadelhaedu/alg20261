for num in range(1, 1000001):
    contador = 0
    for i in range(num):
        if i == 0:
            continue
        if num % i == 0:
            
            contador += 1

    if contador == 1:
        print('número primo:', num)
    

    