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

if nota2 == maiorNota:
    if distancia2 < menorDistancia:
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
