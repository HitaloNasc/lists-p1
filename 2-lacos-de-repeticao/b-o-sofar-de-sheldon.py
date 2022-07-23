# Problem Statement
#
# Sheldon está sentado no sofá da entrada do CIn. No entanto, ele não se encontra satisfeito pois está passando calor, com fome e sua conexão de internet está oscilando. Por isso, ele resolve procurar um lugar perfeitamente calculado para que se sinta mais acomodado.
#
# Sofá
#
# No início, as condições se encontram da seguinte maneira:
#
# Temperatura = 30 graus
# Fome = Com fome
# Internet = 0mb/s
# Input
#
# Você receberá indeterminadas entradas contendo ações realizadas pelo Sheldon para resolver a situação, até receber a entrada “parar”. As ações podem ser as seguintes:
#
# ir para o grad → Diminui a Temperatura em 5 graus e aumenta a Internet em 300mb/s
#
# sair para a rua → Aumenta a Temperatura em 5 graus
#
# comer uma quentinha → Acaba com a fome de Sheldon
#
# conectar no wifi → Aumenta a Internet em 100mb/s
#
# parar → Sempre será a última entrada
#
# Output
#
# Caso receba uma entrada inválida, imprima e continue o programa:
# Entrada inválida
#
# Ao final das N entradas, seu código deverá imprimir, na seguinte ordem:
# -Caso a temperatura seja de 30 graus ou superior:
#
# A temperatura aqui não está agradável
#
# -Caso a temperatura seja de 25 graus ou inferior:
#
# Agora sim, está aconchegante
#
# Caso Sheldon esteja com fome:
#
# Meu corpo precisa de comida
#
# -Caso a Internet esteja abaixo de 100mb/s:
#
# Essa conexão está horrível
#
# Por fim, independente das saídas anteriores, caso Sheldon esteja sem fome, a temperatura esteja de 25 graus ou inferior e a conexão seja igual ou maior 300mb/s, seu código deverá imprimir:
# Finalmente um lugar preciso para mim!
#
# Examples
#
# Case: 1
#
# Input
#
# ir para o grad
# comer uma quentinha
# conectar no wifi
# parar
#
# Output
#
# Agora sim, está aconchegante
# Finalmente um lugar preciso para mim!
#
# Case: 2
#
# Input
#
# comer uma quentinha
# sair para a rua
# parar
#
# Output
#
# A temperatura aqui não está agradável
# Essa conexão está horrível
#

# condições iniciais
temperatura = 30
fome = True
internet = 0

condicao_parada = True
while condicao_parada:
    entrada = input()

    if entrada == 'ir para o grad':
        temperatura -= 5
        internet += 300
    elif entrada == 'sair para a rua':
        temperatura += 5
    elif entrada == 'comer uma quentinha':
        fome = False
    elif entrada == 'conectar no wifi':
        internet += 100
    elif entrada == 'parar':
        condicao_parada = False
    else:
        print('Entrada inválida')

temperatura_ok = False
fome_ok = False
internet_ok = False

if temperatura >= 30:
    print('A temperatura aqui não está agradável')
elif temperatura <= 25:
    temperatura_ok = True
    print('Agora sim, está aconchegante')

if fome:
    print('Meu corpo precisa de comida')
else:
    fome_ok = True

if internet < 100:
    print('Essa conexão está horrível')
else:
    internet_ok = True

if temperatura_ok and fome_ok and internet_ok:
    print('Finalmente um lugar preciso para mim!')
