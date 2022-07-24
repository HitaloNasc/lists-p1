# Problem Statement
#
# Bazainga
#
# Sheldon Lee Cooper se prova constantemente, na série, um dos homens mais inteligentes do mundo desde criança, mas para conseguir o seu objetivo final, ganhar o Nobel de Física, ele precisa da sua ajuda.
#
# Para isso, Sheldon pediu para você listar as conquistas acadêmicas que ele terá na sua vida até chegar no prêmio Nobel. Você terá que se certificar não só quais são os feitos que Sheldon realizou, mas se eles estão vindo na ordem cronologicamente correta também, sendo eles, já em ordem:
#
# 'Começou a Trabalhar na Caltech', 'Trabalho sobre a String Theory', 'Ganhar o Chancellor de ciência', 'Pensar na Teoria de Cooper-Hofstader', 'Criou a Super Assimetria' e 'Ganhar o Nobel'.
#
# Sheldon é conhecido pelas suas pegadinhas também, então, se assim que ele completar um desses feitos, a palavra 'Bazinga' for recebida, o feito deve ser desconsiderado, e precisará ser feito novamente para ser validado. Atenção, se você receber um Bazinga sem ser logo após ele ter ‘avançado’ mais um feito na sua carreira, ele não deve retroceder de novo.
#
# Sheldon também pode ser um pouco duro com seus amigos, então, se ele xingar Howard, Leonard ou Raj, você deve repreender ele!
#
# Obs.: Se você receber algum desses feitos na ordem errada, ele não deve ser considerado como feito, e só como uma mensagem recebida.
#
# Input
#
# Você receberá vários inputs em forma de mensagem, e só não irá mais recebê-los quando Sheldon ganhar o Nobel ou quando receber a mensagem: ‘É o fim da Estrada pra Sheldon Cooper’.
#
# Mensagem 1
# Mensagem 2
# Mensagem 3
# .
# .
# .
# Mensagem N
# Output
#
# Se você receber os xingamentos: 'Tinha que ser o engenheiro sem Phd do Wolowitz' ou 'Leonard seu anão covarde' ou 'Tu é muito burro Raj’, você deve printar:
#
# Não xingue seus amigos Sheldon!
#
# No fim de tudo, se Sheldon desistir antes mesmo de Começou a Trabalhar na Caltech, deve ser printado:
#
# Que potencial desperdiçado...
#
# Se ele ainda estiver apenas Trabalhando na String Theory ou na Caltech, printe:
#
# Tão perto, mas tão longe
#
# Se ele ainda estiver até só ter ganho o Chancellor ou pensado na Teoria de Cooper-Hofstader, printe:
#
# Não desista Sheldon, você ainda têm muito para alcançar!
#
# Se ele tiver pensado na Super Assimetria, mas ainda não ganho o Nobel, printe:
#
# Nãoooooo, esse momento ia ser seu Sheldon
#
# Se ele tiver ganho o Nobel, printe:
#
# Você conseguiu Sheldon, o Nobel é seu!!!
#
# Examples
#
# Case: 1
#
# Input
#
# Começou a Trabalhar na Caltech
# Trabalho sobre a String Theory
# Tinha que ser o engenheiro sem Phd do Wolowitz
# Ganhar o Chancellor de ciência
# Bazinga
# Ganhar o Chancellor de ciência
# Pensar na Teoria de Cooper-Hofstader
# Zoar a Penny
# Bazinga
# Criou a Super Assimetria
# Ganhar o Nobel
#
# Output
#
# Não xingue seus amigos Sheldon!
# Você conseguiu Sheldon, o Nobel é seu!!!
#
# Case: 2
#
# Input
#
# Começou a Trabalhar na Caltech
# Bazinga
# Leonard seu anão covarde
# Começou a Trabalhar na Caltech
# Trabalho sobre a String Theory
# Amy é linda demais
# Pensar na Teoria de Cooper-Hofstader
# Bazinga
# Tu é muito burro Raj
# Bazinga
# É o fim da Estrada pra Sheldon Cooper
#
# Output
#
# Não xingue seus amigos Sheldon!
# Não xingue seus amigos Sheldon!
# Tão perto, mas tão longe

ETAPA_1 = 'Começou a Trabalhar na Caltech'
ETAPA_2 = 'Trabalho sobre a String Theory'
ETAPA_3 = 'Ganhar o Chancellor de ciência'
ETAPA_4 = 'Pensar na Teoria de Cooper-Hofstader'
ETAPA_5 = 'Criou a Super Assimetria'
ETAPA_6 = 'Ganhar o Nobel'

ETAPA_1_OK = False
ETAPA_2_OK = False
ETAPA_3_OK = False
ETAPA_4_OK = False
ETAPA_5_OK = False
ETAPA_6_OK = False

XINGAMENTO_1 = 'Tinha que ser o engenheiro sem Phd do Wolowitz'
XINGAMENTO_2 = 'Leonard seu anão covarde'
XINGAMENTO_3 = 'Tu é muito burro Raj'

DESISTIIU = 'É o fim da Estrada pra Sheldon Cooper'

BAZINGA = 'Bazinga'

ultima_entrada = ''

condicao_parada = True
while condicao_parada:
    entrada = input()

    # verifica se a entrada atual é um avanço
    eAvanco = entrada == ETAPA_1 or entrada == ETAPA_2 or entrada == ETAPA_3 or entrada == ETAPA_4 or entrada == ETAPA_5 or entrada == ETAPA_6
    # verifica se a última entrada foi um avanço
    foiAvanco = ultima_entrada == ETAPA_1 or ultima_entrada == ETAPA_2 or ultima_entrada == ETAPA_3 or ultima_entrada == ETAPA_4 or ultima_entrada == ETAPA_5 or ultima_entrada == ETAPA_6

    # Achando o último avanço
    ULTIMA_1 = ETAPA_1_OK and not ETAPA_2_OK
    ULTIMA_2 = ETAPA_2_OK and not ETAPA_3_OK
    ULTIMA_3 = ETAPA_3_OK and not ETAPA_4_OK
    ULTIMA_4 = ETAPA_4_OK and not ETAPA_5_OK
    ULTIMA_5 = ETAPA_5_OK and not ETAPA_6_OK
    ULTIMA_6 = ETAPA_6_OK

    if eAvanco:
        if entrada == ETAPA_1:
            if not ETAPA_1_OK:
                # print('etapa 1')
                ETAPA_1_OK = True
        elif entrada == ETAPA_2:
            if ETAPA_1_OK and not ETAPA_2_OK:
                # print('etapa 2')
                ETAPA_2_OK = True
        elif entrada == ETAPA_3:
            if ETAPA_1_OK and ETAPA_2_OK and not ETAPA_3_OK:
                # print('etapa 3')
                ETAPA_3_OK = True
        elif entrada == ETAPA_4:
            if ETAPA_1_OK and ETAPA_2_OK and ETAPA_3_OK and not ETAPA_4_OK:
                # print('etapa 4')
                ETAPA_4_OK = True
        elif entrada == ETAPA_5:
            if ETAPA_1_OK and ETAPA_2_OK and ETAPA_3_OK and ETAPA_4_OK and not ETAPA_5_OK:
                # print('etapa 5')
                ETAPA_5_OK = True
        elif entrada == ETAPA_6:
            if ETAPA_1_OK and ETAPA_2_OK and ETAPA_3_OK and ETAPA_4_OK and ETAPA_5_OK and not ETAPA_6_OK:
                # print('etapa 6')
                ETAPA_6_OK = True
                print('Você conseguiu Sheldon, o Nobel é seu!!!')
                condicao_parada = False
    elif entrada == BAZINGA:
        if foiAvanco:
            if ultima_entrada == ETAPA_1:
                ETAPA_1_OK = False
            elif ultima_entrada == ETAPA_2:
                ETAPA_2_OK = False
            elif ultima_entrada == ETAPA_3:
                ETAPA_3_OK = False
            elif ultima_entrada == ETAPA_4:
                ETAPA_4_OK = False
            elif ultima_entrada == ETAPA_5:
                ETAPA_5_OK = False
            elif ultima_entrada == ETAPA_6:
                ETAPA_6_OK = False
    elif entrada == XINGAMENTO_1 or entrada == XINGAMENTO_2 or entrada == XINGAMENTO_3:
        print('Não xingue seus amigos Sheldon!')
    elif entrada == DESISTIIU:
        if ULTIMA_1 or ULTIMA_2:
            print('Tão perto, mas tão longe')
        elif ULTIMA_3 or ULTIMA_4:
            print('Não desista Sheldon, você ainda têm muito para alcançar!')
        elif ULTIMA_5:
            print('Nãoooooo, esse momento ia ser seu Sheldon')
        else:
            print('Que potencial desperdiçado...')
        condicao_parada = False

    ultima_entrada = entrada
