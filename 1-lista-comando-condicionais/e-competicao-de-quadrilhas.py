nome_da_quadrilha = input()
passo_1 = input()
passo_2 = input()
passo_3 = input()
passo_4 = input()
passo_5 = input()

CUMPRIMENTO = 'Cumprimento'
BALANCE = 'Balancê'
PASSEIO = 'Passeio'
TUNEL = 'Túnel'
SERROTE = 'Serrote'
CASAMENTO = 'Casamento'
DESPEDIDA = 'Despedida'

pontuacao = 0.0
ocorreu_casamento = False
usou_passo_invalido = False

# passo_1
if passo_1 == CUMPRIMENTO:
    pontuacao += 100
elif passo_1 == BALANCE:
    pontuacao += 50
elif passo_1 == PASSEIO:
    pontuacao += 70
elif passo_1 == TUNEL:
    pontuacao *= 0.9
elif passo_1 == SERROTE:
    pontuacao += 100
elif passo_1 == CASAMENTO:
    ocorreu_casamento = True
elif passo_1 == DESPEDIDA:
    pontuacao += 0
else:
    usou_passo_invalido = True

# passo_2
if passo_2 == CUMPRIMENTO:
    pontuacao += 10
elif passo_2 == BALANCE:
    pontuacao += 50
elif passo_2 == PASSEIO:
    pontuacao += 70
elif passo_2 == TUNEL:
    pontuacao *= 0.9
elif passo_2 == SERROTE:
    pontuacao += 100
elif passo_2 == CASAMENTO:
    ocorreu_casamento = True
elif passo_2 == DESPEDIDA:
    pontuacao += 0
else:
    usou_passo_invalido = True

# passo_3
if passo_3 == CUMPRIMENTO:
    pontuacao += 10
elif passo_3 == BALANCE:
    pontuacao += 50
elif passo_3 == PASSEIO:
    pontuacao += 70
elif passo_3 == TUNEL:
    pontuacao *= 0.9
elif passo_3 == SERROTE:
    pontuacao += 100
elif passo_3 == CASAMENTO:
    ocorreu_casamento = True
elif passo_3 == DESPEDIDA:
    pontuacao += 0
else:
    usou_passo_invalido = True

# passo_4
if passo_4 == CUMPRIMENTO:
    pontuacao += 10
elif passo_4 == BALANCE:
    pontuacao += 50
elif passo_4 == PASSEIO:
    pontuacao += 70
elif passo_4 == TUNEL:
    pontuacao *= 0.9
elif passo_4 == SERROTE:
    pontuacao += 100
elif passo_4 == CASAMENTO:
    ocorreu_casamento = True
elif passo_4 == DESPEDIDA:
    pontuacao += 0
else:
    usou_passo_invalido = True

# passo_5
if passo_5 == CUMPRIMENTO:
    pontuacao += 10
elif passo_5 == BALANCE:
    pontuacao += 50
elif passo_5 == PASSEIO:
    pontuacao += 70
elif passo_5 == TUNEL:
    pontuacao *= 0.9
elif passo_5 == SERROTE:
    pontuacao += 100
elif passo_5 == CASAMENTO:
    ocorreu_casamento = True
elif passo_5 == DESPEDIDA:
    pontuacao += 35
else:
    usou_passo_invalido = True

if ocorreu_casamento:
    pontuacao *= 2

if usou_passo_invalido:
    pontuacao = 0.0

if pontuacao == 0:
    print(
        "Poxa, {nome_da_quadrilha}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.".format(
            nome_da_quadrilha=nome_da_quadrilha))
else:
    print("Parabéns, {nome_da_quadrilha}! Bela apresentação. A pontuação foi de {pontuacao:.1f}!".format(
        nome_da_quadrilha=nome_da_quadrilha, pontuacao=pontuacao))
