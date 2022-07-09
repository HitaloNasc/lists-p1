# Problem Statement
#
# Os calouros pós-pandemia estão subindo as paredes e loucos por uma calourada, portanto no clima tardio de São João
# eles receberão sua própria Barraca do Beijo na QuermeCin. Não precisa pagar nada! Apenas escolher um número de 1 a
# 5 para testar sua sorte e saber de quem você vai receber uma bitoca.
#
# https://s2.glbimg.com/K8xVdH_LS6xNb0skgM3U_lVGlfs=/e.glbimg.com/og/ed/f/original/2018/02/10/gretchen_e_carlos_marques-1-2.jpg
#
# Input
#
# Você receberá um número inteiro:
#
# numero (int)
#
# Output
#
# Se for número 1 imprima: “Você tirou o Doguinho! Vai receber muitos lambeijos!”
#
# Se for o número 2: “Gabriel Queiroz, eu escolho você! Aí vem o galã da monitoria te tascar um beijão!”
#
# Se for número 3: “Que azar! Não vai beijar ninguém! Tome uma língua de gato de prêmio de consolação…”
#
# Se for número 4: “Olha só! O misterioso monitor de branco vem te entregar uma lista para fazer e um selinho de
# encorajamento!”
#
# Se for número 5: “Ca-Calegário?!!! Ganhou um Hi-5 e um projeto de IP/P1 para entregar daqui a duas semanas!”
#
# Se digitar qualquer outro número: “Véi! São 5 opções, não é difícil escolher…”
#
# Examples
#
# Case: 1
#
# Input
#
# 2
#
# Output
#
# Gabriel Queiroz, eu escolho você! Aí vem o galã da monitoria te tascar um beijão!

number = int(input())
response = 'Véi! São 5 opções, não é difícil escolher…'

if number == 1:
    response = 'Você tirou o Doguinho! Vai receber muitos lambeijos!'
elif number == 2:
    response = 'Gabriel Queiroz, eu escolho você! Aí vem o galã da monitoria te tascar um beijão!'
elif number == 3:
    response = 'Que azar! Não vai beijar ninguém! Tome uma língua de gato de prêmio de consolação…'
elif number == 4:
    response = 'Olha só! O misterioso monitor de branco vem te entregar uma lista para fazer e um selinho de ' \
               'encorajamento! '
elif number == 5:
    response = 'Ca-Calegário?!!! Ganhou um Hi-5 e um projeto de IP/P1 para entregar daqui a duas semanas!'

print(response)
