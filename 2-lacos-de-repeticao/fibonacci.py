distancia = 13
ultimo = 1
penultimo = 1

if distancia > 2:
    termo = 3
    while termo < distancia:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
    #  count += 1
    print(termo)
