nome_1 = input()
pontuacao_1 = int(input())
nome_2 = input()
pontuacao_2 = int(input())
nome_3 = input()
pontuacao_3 = int(input())

nome_primeiro_lugar = nome_1
pontuacao_primeiro_lugar = pontuacao_1
nome_segundo_lugar = nome_1
pontuacao_segundo_lugar = pontuacao_1
nome_terceiro_lugar = nome_1
pontuacao_terceiro_lugar = pontuacao_1

# definir primeiro e segundo lugar
if pontuacao_2 < pontuacao_primeiro_lugar:
    nome_segundo_lugar = nome_primeiro_lugar
    pontuacao_segundo_lugar = pontuacao_primeiro_lugar
    nome_primeiro_lugar = nome_2
    pontuacao_primeiro_lugar = pontuacao_2
elif pontuacao_2 == pontuacao_primeiro_lugar:
    if len(nome_2) < len(nome_primeiro_lugar):
        nome_segundo_lugar = nome_primeiro_lugar
        pontuacao_segundo_lugar = pontuacao_primeiro_lugar
        nome_primeiro_lugar = nome_2
        pontuacao_primeiro_lugar = pontuacao_2
    else:
        nome_segundo_lugar = nome_2
        pontuacao_segundo_lugar = pontuacao_2
else:
    nome_segundo_lugar = nome_2
    pontuacao_segundo_lugar = pontuacao_2

# definir terceiro lugar
if pontuacao_3 < pontuacao_primeiro_lugar:
    nome_terceiro_lugar = nome_segundo_lugar
    nome_segundo_lugar = nome_primeiro_lugar
    nome_primeiro_lugar = nome_3
    pontuacao_terceiro_lugar = pontuacao_segundo_lugar
    pontuacao_segundo_lugar = pontuacao_primeiro_lugar
    pontuacao_primeiro_lugar = pontuacao_3
elif pontuacao_3 == pontuacao_primeiro_lugar:
    if len(nome_3) < len(nome_primeiro_lugar):
        nome_terceiro_lugar = nome_segundo_lugar
        nome_segundo_lugar = nome_primeiro_lugar
        nome_primeiro_lugar = nome_3
        pontuacao_terceiro_lugar = pontuacao_segundo_lugar
        pontuacao_segundo_lugar = pontuacao_primeiro_lugar
        pontuacao_primeiro_lugar = pontuacao_3
    else:
        if pontuacao_3 < pontuacao_segundo_lugar:
            nome_terceiro_lugar = nome_segundo_lugar
            nome_segundo_lugar = nome_3
            pontuacao_terceiro_lugar = pontuacao_segundo_lugar
            pontuacao_segundo_lugar = pontuacao_3
        elif pontuacao_3 == pontuacao_segundo_lugar:
            if len(nome_3) < len(nome_segundo_lugar):
                nome_terceiro_lugar = nome_segundo_lugar
                nome_segundo_lugar = nome_3
                pontuacao_terceiro_lugar = pontuacao_segundo_lugar
                pontuacao_segundo_lugar = pontuacao_3
            else:
                nome_terceiro_lugar = nome_3
                pontuacao_terceiro_lugar = pontuacao_3
        else:
            nome_terceiro_lugar = nome_3
            pontuacao_terceiro_lugar = pontuacao_3
elif pontuacao_primeiro_lugar < pontuacao_3 < pontuacao_segundo_lugar:
    print('entrei')
    nome_terceiro_lugar = nome_segundo_lugar
    nome_segundo_lugar = nome_3
    pontuacao_terceiro_lugar = pontuacao_segundo_lugar
    pontuacao_segundo_lugar = pontuacao_3
elif pontuacao_3 > pontuacao_primeiro_lugar and pontuacao_3 == pontuacao_segundo_lugar:
    print('aqui')
    if len(nome_3) < len(nome_segundo_lugar):
        nome_terceiro_lugar = nome_segundo_lugar
        nome_segundo_lugar = nome_3
        pontuacao_terceiro_lugar = pontuacao_segundo_lugar
        pontuacao_segundo_lugar = pontuacao_3
    else:
        nome_terceiro_lugar = nome_3
        pontuacao_terceiro_lugar = pontuacao_3
else:
    nome_terceiro_lugar = nome_3
    pontuacao_terceiro_lugar = pontuacao_3

print('{0} {1}'.format(nome_primeiro_lugar, pontuacao_primeiro_lugar))
print('{0} {1}'.format(nome_segundo_lugar, pontuacao_segundo_lugar))
print('{0} {1}'.format(nome_terceiro_lugar, pontuacao_terceiro_lugar))


