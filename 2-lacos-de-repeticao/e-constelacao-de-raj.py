entrada = int(input())

if entrada > 3:
    aux_x = 0
    aux_z = 0
    soma_distancias = 0
    count_not_fibonacci = 0

    count = 0
    while count < entrada:
        x = int(input())
        z = int(input())

        if count != 0:
            distancia = int(((aux_x - x) ** 2 + (aux_z - z) ** 2) ** 0.5)
            print('Distância [star{a} <-> star{b}]: {distancia}'.format(a=count, b=count + 1, distancia=distancia))
            soma_distancias += distancia

            # verificar se a distância é um número fibonacci
            ultimo = 1
            penultimo = 1
            if distancia > 2:
                termo = 3
                while termo < distancia:
                    termo = ultimo + penultimo
                    penultimo = ultimo
                    ultimo = termo
                if termo != distancia:
                    count_not_fibonacci += 1

        aux_x = x
        aux_z = z
        count += 1

    # verificar se a soma é primo
    eSomaPrimo = False
    mult = 0
    for i in range(2, soma_distancias):
        if soma_distancias % i == 0:
            mult += 1
    if mult == 0:
        eSomaPrimo = True

    # ferificar se todos são da sequência fibonacci
    todos_fibonacci = False
    if count_not_fibonacci == 0:
        todos_fibonacci = True

    # definir saídas
    if todos_fibonacci and not eSomaPrimo:
        print('Yes! Eu consegui!')
    elif todos_fibonacci and eSomaPrimo:
        print('Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!')
    elif not todos_fibonacci and count_not_fibonacci == 1:
        print('Oh, não! Eu quase consegui!')
    elif not eSomaPrimo and count_not_fibonacci >= 2:
        print('Eu vou acabar como o Stuart :/')
    elif eSomaPrimo and count_not_fibonacci >= 2:
        print('Pelo menos o programa está funcionando...')
elif 3 > entrada > 0:
    print('Acho que bebi demais, eu juro que tinha mais estrelas!')
else:
    print('Isso está quebrado, acho que Howard pode me ajudar.')
