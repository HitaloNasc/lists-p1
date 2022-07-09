# Problem Statement
#
# Originalmente criadas para celebras os três santos de junho – Antônio, João e Pedro -, as festas juninas começaram
# a tomar conta da agenda cultura do Brasil. De norte a sul, as cidades convidam a população e os turistas para
# festejos típicos. As principais cidades são: Caruaru(PE), Campina Grande(PB), João Pessoa(PB), São Luís (MA),
# Mossoró e Natal (RN), Fortaleza (CE), entre outas. Para escolher a melhor festa, existe um site que fornece notas,
# que é uma média das avaliações recebidas por cada cidade. Sua tarefa é ajudar o usuário a encontrar a cidade mais
# adequada para ele ir, que seria a de maior nota. Apenas um detalhe, caso a nota mais alta não seja maior ou igual a
# 4, deve-se imprimir "Nota mínima não atingida".
#
# Em caso de empate nas notas deve selecionar a cidade mais próxima. Não haverá empate na proximidade nesses casos.
#
# Input
#
# As entradas representam as informações de 3 cidades, para cada cidade, teremos uma string composta pelo nome da
# cidade, seguido da respectiva nota (0 <= nota <= 5.0, com 1 casa decimal) e a distância da cidade em relação ao
# usuário em km,
#
# Cidade 1
#
# Nota 1
#
# Distância 1
#
# Cidade 2
#
# Nota 2
#
# Distância 2
#
# Cidade 3
#
# Nota 3
#
# Distância 3
#
# Output
#
# A saída consiste de uma linha única
#
# Caso nenhuma cidade tenha nota maior ou igual a 4:
#
# Nota mínima não atingida
#
# Caso contrário, você deve imprimir a cidade com a maior pontuação
#
# Nome_Cidade
#
# Examples
#
# Case: 1
#
# Input
#
# Campina Grande
# 3.5
# 1150
# Caruaru
# 4.0
# 1140
# Recife
# 3.5
# 1570
#
# Output
#
# Caruaru
#
# Case: 2
#
# Input
#
# Fortaleza
# 3.5
# 1150
# Natal
# 3.0
# 1060
# Mossoro
# 3.5
# 1570
#
# Output
#
# Nota mínima não atingida
#
# Case: 3
#
# Input
#
# Salvador
# 4.0
# 1150
# Paulo Afonso
# 4.0
# 1060
# Aracaju
# 4.0
# 1570
#
# Output
#
# Paulo Afonso

cidade1 = input()
nota1 = float(input())
distancia1 = int(input())
cidade2 = input()
nota2 = float(input())
distancia2 = int(input())
cidade3 = input()
nota3 = float(input())
distancia3 = int(input())

melhorCidade = cidade1
maiorNota = nota1
menorDistancia = distancia1
resposta = ''

if nota2 > maiorNota:
    maiorNota = nota2
    melhorCidade = cidade2
    menorDistancia = distancia2

if nota2 == maiorNota and distancia2 < menorDistancia:
    maiorNota = nota2
    melhorCidade = cidade2
    menorDistancia = distancia2

if nota3 > maiorNota:
    maiorNota = nota3
    melhorCidade = cidade3
    menorDistancia = distancia3

if nota3 == maiorNota:
    if distancia3 < menorDistancia:
        maiorNota = nota3
        melhorCidade = cidade3
        menorDistancia = distancia3

if maiorNota < 4.0:
    resposta = "Nota mínima não atingida"
else:
    resposta = melhorCidade

print(resposta)
