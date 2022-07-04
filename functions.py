def cria_tabela(tabela):
    jogo_da_velha = ""
    for i in range(len(tabela)):
        if i == 2 or i == 5 or i == 8:
            jogo_da_velha += " " + tabela[i] + " \n"
        else:
            jogo_da_velha += " " + tabela[i] + " |"
    return jogo_da_velha


def verifica_posicao(tabela, posicao):
    result = False
    if tabela[posicao] == "_":
        result = True
    return result


def verifica_vitoria(tabela, simbolo):
    result = False
    # horizontais
    if tabela[0] == simbolo and tabela[1] == simbolo and tabela[2] == simbolo:
        result = True

    elif tabela[3] == simbolo and tabela[4] == simbolo and tabela[5] == simbolo:
        result = True

    elif tabela[6] == simbolo and tabela[7] == simbolo and tabela[8] == simbolo:
        result = True
    # vertical
    elif tabela[0] == simbolo and tabela[3] == simbolo and tabela[6] == simbolo:
        result = True

    elif tabela[1] == simbolo and tabela[4] == simbolo and tabela[7] == simbolo:
        result = True

    elif tabela[2] == simbolo and tabela[5] == simbolo and tabela[8] == simbolo:
        result = True

    # diagonal
    elif tabela[0] == simbolo and tabela[4] == simbolo and tabela[8] == simbolo:
        result = True

    elif tabela[2] == simbolo and tabela[4] == simbolo and tabela[6] == simbolo:
        result = True

    return result


def verifica_empate(tabela):
    result = True
    for i in tabela:
        if i == "_":
            result = False
    return result
