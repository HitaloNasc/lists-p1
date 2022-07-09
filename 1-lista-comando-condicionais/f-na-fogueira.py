# Problem Statement
#
# Bruna e Frej organizaram no São João uma viagem com os amigos para Gravatá. O grupo passaria de quinta a domingo em
# uma casa, além de que no sábado iriam para a festa Carvalheira. Todos estavam muito animados para o dia 25/06 pois
# iria tocar Jorge e Mateus, Xand Avião, Felipe Amorim e muito mais...
#
# Mas como a cidade estava um caos de trânsito e super lotação, nenhum deles queria ir dirigindo. Como Bruna e Frej
# são os donos da casa e são muito inteligentes, eles fizeram uma competição com os outros 3 amigos (Artur,
# Rodrigo e Lucas) para saber quem iria dirigindo para o show.
#
# foto da festa
#
# Os três começam com zero pontos e sua pontuação aumenta sempre que eles cometem um erro. Ou seja, VENCE AQUELE COM
# A MENOR PONTUAÇÃO.
#
# Em casos de empate, vence o jogador com o nome lexicograficamente menor e a ordem dos nomes pode mudar.
#
# Por mais que Bruna e Frej sejam muito espertos, eles querem ajuda em como organizar a ordem desses amigos nesse
# torneio do São João 2022, por isso chamaram você! Determine o primeiro, segundo e terceiro lugar, nessa ordem,
# dado os nomes e pontuações dos amigos em cada partida.
#
# Obs: não use max(), min() ou outras funções externas semelhantes. Não use funções externas para ordenação.
#
# Input
#
# A entrada consiste de seis linhas, contendo os nomes e pontuações finais de cada competidor.
#
# Nome e pontuação (inteiro) do primeiro amigo:
#
# nome_1
#
# pontuação_1
#
# Nome e pontuação (inteiro) do segundo amigo:
#
# nome_2
#
# pontuação_2
#
# Nome e pontuação (inteiro) do terceiro amigo:
#
# nome_3
#
# pontuação_3
#
# Output
#
# A saída consiste em três linhas, contendo os pares de nome e pontuação de cada amigo, em ordem do melhor candidato
# para o pior, com os critérios descritos no enunciado.
#
# nome e pontuação do primeiro colocado
#
# nome_primeiro pontuação_primeiro
#
# nome e pontuação do segundo colocado
#
# nome_segundo pontuação_segundo
#
# nome e pontuação do terceiro colocado
#
# nome_terceiro pontuação_terceiro
#
# Examples
#
# Case: 1
#
# Input
#
# Rodrigo
# 3
# Lucas
# 4
# Artur
# 1
#
# Output
#
# Artur 1
# Rodrigo 3
# Lucas 4
#
# Case: 2
#
# Input
#
# Artur
# 10
# Lucas
# 2
# Rodrigo
# 5
#
# Output
#
# Lucas 2
# Rodrigo 5
# Artur 10

nome_1 = input()
pontuacao_1 = int(input())
nome_2 = input()
pontuacao_2 = int(input())
nome_3 = input()
pontuacao_3 = int(input())

# primeiro lugar
nome_primeiro_lugar = nome_1
pontuacao_primeiro_lugar = pontuacao_1
# segundo lugar
nome_segundo_lugar = nome_1
pontuacao_segundo_lugar = pontuacao_1
# terceiro lugar
nome_terceiro_lugar = nome_1
pontuacao_terceiro_lugar = pontuacao_1

# comparação do valor 2 com valor 1
if pontuacao_2 < pontuacao_primeiro_lugar:
    # segundo lugar parcial
    pontuacao_segundo_lugar = pontuacao_primeiro_lugar
    nome_segundo_lugar = nome_primeiro_lugar
    # primeiro lugar parcial
    pontuacao_primeiro_lugar = pontuacao_2
    nome_primeiro_lugar = nome_2
else:
    if pontuacao_2 == pontuacao_primeiro_lugar:
        if nome_2 < nome_primeiro_lugar:
            # segundo lugar parcial
            pontuacao_segundo_lugar = pontuacao_primeiro_lugar
            nome_segundo_lugar = nome_primeiro_lugar
            # primeiro lugar parcial
            pontuacao_primeiro_lugar = pontuacao_2
            nome_primeiro_lugar = nome_2
        else:
            # segundo lugar parcial
            pontuacao_segundo_lugar = pontuacao_2
            nome_segundo_lugar = nome_2
    else:
        if pontuacao_2 > pontuacao_primeiro_lugar:
            # segundo lugar parcial
            pontuacao_segundo_lugar = pontuacao_2
            nome_segundo_lugar = nome_2

# comparação do valor 3 com os demais
if pontuacao_3 < pontuacao_primeiro_lugar:
    # terceiro lugar parcial
    pontuacao_terceiro_lugar = pontuacao_segundo_lugar
    nome_terceiro_lugar = nome_segundo_lugar
    # segundo lugar parcial
    pontuacao_segundo_lugar = pontuacao_primeiro_lugar
    nome_segundo_lugar = nome_primeiro_lugar
    # primeiro lugar parcial
    pontuacao_primeiro_lugar = pontuacao_3
    nome_primeiro_lugar = nome_3
else:
    if pontuacao_3 == pontuacao_primeiro_lugar:
        if nome_3 < nome_primeiro_lugar:
            # terceiro lugar parcial
            pontuacao_terceiro_lugar = pontuacao_segundo_lugar
            nome_terceiro_lugar = nome_segundo_lugar
            # segundo lugar parcial
            pontuacao_segundo_lugar = pontuacao_primeiro_lugar
            nome_segundo_lugar = nome_primeiro_lugar
            # primeiro lugar parcial
            pontuacao_primeiro_lugar = pontuacao_3
            nome_primeiro_lugar = nome_3
        else:
            # terceiro lugar
            pontuacao_terceiro_lugar = pontuacao_segundo_lugar
            nome_terceiro_lugar = nome_segundo_lugar
            # segundo lugar
            pontuacao_segundo_lugar = pontuacao_3
            nome_segundo_lugar = nome_3
    else:
        if pontuacao_3 < pontuacao_segundo_lugar:
            # terceiro lugar
            pontuacao_terceiro_lugar = pontuacao_segundo_lugar
            nome_terceiro_lugar = nome_segundo_lugar
            # segundo lugar
            pontuacao_segundo_lugar = pontuacao_3
            nome_segundo_lugar = nome_3
        else:
            if pontuacao_3 == pontuacao_segundo_lugar:
                if nome_3 < nome_segundo_lugar:
                    # terceiro lugar
                    pontuacao_terceiro_lugar = pontuacao_segundo_lugar
                    nome_terceiro_lugar = nome_segundo_lugar
                    # segundo lugar
                    pontuacao_segundo_lugar = pontuacao_3
                    nome_segundo_lugar = nome_3
                else:
                    # terceiro lugar
                    pontuacao_terceiro_lugar = pontuacao_3
                    nome_terceiro_lugar = nome_3
            else:
                if pontuacao_3 > pontuacao_segundo_lugar:
                    # terceiro lugar
                    pontuacao_terceiro_lugar = pontuacao_3
                    nome_terceiro_lugar = nome_3

print('{0} {1}'.format(nome_primeiro_lugar, pontuacao_primeiro_lugar))
print('{0} {1}'.format(nome_segundo_lugar, pontuacao_segundo_lugar))
print('{0} {1}'.format(nome_terceiro_lugar, pontuacao_terceiro_lugar))
