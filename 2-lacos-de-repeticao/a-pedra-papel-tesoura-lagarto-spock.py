# Problem Statement
#
# Sheldon e Rajesh estão trabalhando juntos e dividindo a mesma sala de trabalho. Raj resolve pedir para colocar uma mesa para ele na sala e Sheldon insiste que não há necessidade, já que a sala é sua e não de Raj. Após muito debate eles resolvem decidir se Raj pode ou não ter uma mesa através de uma série de rodadas de Pedra-papel-tesoura-lagarto-Spock, uma versão do clássico Pedra-papel-tesoura.
#
# gif pptls
#
# Porém, para fins de simplificação eles decidiram que só podem usar a "tesoura", "lagarto" e "spock". As regras são as seguinte:
#
# lagarto envenena spock
# spock quebra tesoura
# tesoura decapita lagarto
# se os dois participantes escolhem o mesmo elemento, ninguém ganha
# Você foi o escolhido para dar o resultado final das rodadas.
#
# Input
#
# A 1ª linha da entrada será um número “N”, esse número representa o total de rodadas. (N > 0)
#
# Após a primeira linha será dado as escolhas de Sheldon e Raj, cada um em uma linha e sempre nessa ordem. Isso irá se repetir N vezes.
#
# Exemplo:
#
# N
#
# escolha_sheldon1
#
# escolha_raj1
#
# …
#
# escolha_sheldonN
#
# escolha_rajN
#
# Output
#
# Ao final das rodadas você deve imprimir o seguinte:
#
# Caso Sheldon tenha ganhado mais partidas:
#
# "BAZINGA! EU SOU O SENHOR DA SALA!"
#
# Caso Raj tenha ganhado mais partidas:
#
# "ENGOLE ESSA, SHELDON!"
#
# Caso eles ganhem o mesmo número de partidas ou hajam apenas empates:
#
# "Oh não, precisamos de outra rodada."
#
# Examples
#
# Case: 1
#
# Input
#
# 3
# lagarto
# spock
# tesoura
# spock
# spock
# tesoura
#
# Output
#
# BAZINGA! EU SOU O SENHOR DA SALA!
#
# Case: 2
#
# Input
#
# 4
# spock
# lagarto
# tesoura
# spock
# lagarto
# tesoura
# lagarto
# tesoura
#
# Output
#
# ENGOLE ESSA, SHELDON!

# quantidade de partidas
n = int(input())

# contadores
count = 0
score_sheldon = 0
score_raj = 0

# opções
LAGARTO = 'lagarto'
SPOCK = 'spock'
TESOURA = 'tesoura'

while count < n:
    # escolha de sheldon
    sheldon = input()
    # escolha de raj
    raj = input()

    if sheldon == LAGARTO:
        if raj == SPOCK:
            score_sheldon += 1
        elif raj == TESOURA:
            score_raj += 1
    elif sheldon == SPOCK:
        if raj == TESOURA:
            score_sheldon += 1
        elif raj == LAGARTO:
            score_raj += 1
    elif sheldon == TESOURA:
        if raj == LAGARTO:
            score_sheldon += 1
        elif raj == SPOCK:
            score_raj += 1

    count += 1

if score_sheldon > score_raj:
    print("BAZINGA! EU SOU O SENHOR DA SALA!")
elif score_sheldon < score_raj:
    print("ENGOLE ESSA, SHELDON!")
elif score_sheldon == score_raj:
    print("Oh não, precisamos de outra rodada.")
