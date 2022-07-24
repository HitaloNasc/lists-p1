soma_distancias = 251
eSomaPrimo = False
mult = 0
for i in range(2, soma_distancias):
    if soma_distancias % i == 0:
        mult += 1
if mult == 0:
    eSomaPrimo = True

print(f'primo: {eSomaPrimo}')