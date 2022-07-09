# Problem Statement
#
# Foi decidido que no CIN seria feito uma competição de quadrilhas juninas e cada turma deveria participar. Você foi
# o responsável por calcular a pontuação de cada equipe. Uma lista de passos permitidos foi divulgada para cada
# equipe. Algumas regras foram definidas para calcular a pontuação final da quadrilha, mas preste bem atenção,
# somente você tem acesso a essas regras.
#
# gif quadrilha
#
# Lista de passos permitidos:
#
# Cumprimento.
# Balancê.
# Passeio.
# Túnel.
# Serrote.
# Casamento.
# Despedida.
# Regras:
#
# Cada quadrilha tem uma sequência de 5 passos. Se algum passo diferente dos divulgados da lista for usado,
# a quadrilha terá a pontuação zerada. Toda quadrilha que começar com o passo “Cumprimento” terá pontuação inicial de
# 100 pontos. Caso o “Cumprimento” apareça em alguma outra posição, damos 10 pontos. A cada “Balancê” a pontuação é
# acrescida de 50 pontos. Cada “Passeio” vale 70 pontos. Cada vez que fizer o “Túnel” perde 10% da pontuação.
# “Serrote” vale 100 pontos. Caso o casamento seja realizado ao menos uma vez, a pontuação final é dobrada. A
# “Despedida” só será pontuada se vier como último passo da quadrilha, caso apareça em alguma outra posição a
# pontuação não será modificada. A "Despedida" vale 35 pontos. OBS: A pontuação deverá ser do tipo float.
#
# Input
#
# A entrada consiste nas seguintes 6 linhas:
#
# "nome_da_quadrilha"
#
# "passo_1"
#
# "passo_2"
#
# "passo_3"
#
# "passo_4"
#
# "passo_5"
#
# Atenção: As entradas sempre serão amigáveis e nunca uma quadrilha será composta de apenas um único movimento.
#
# Output
#
# Se a pontuação for zero, deverá retornar a seguinte frase:
#
# "Poxa, [nome_da_quadrilha]. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada."
#
# Caso a pontuação seja maior que zero:
#
# "Parabéns, [nome_da_quadrilha]! Bela apresentação. A pontuação foi de [pontuacao]!"
#
# Atenção: A pontuação deverá ser impressa com a precisão de 1 casa decimal.
#
# Examples
#
# Case: 1
#
# Input
#
# CINtenario de tradição
# Cumprimento
# Serrote
# Casamento
# Serrote
# Despedida
#
# Output
#
# Parabéns, CINtenario de tradição! Bela apresentação. A pontuação foi de 670.0!
#
# Case: 2
#
# Input
#
# CINtenario de tradição
# Cumprimento
# Avante
# Casamento
# Serrote
# Despedida
#
# Output
#
# Poxa, CINtenario de tradição. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.
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
