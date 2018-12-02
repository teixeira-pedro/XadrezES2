def isPreta(tabuleiro, xPecaAtual, yPecaAtual):
    pecaAtual = tabuleiro[xPecaAtual][yPecaAtual]
    if (pecaAtual.isupper()):
        return 1
    return 0


def isPecaAliada(tabuleiro, xPecaAtual, yPecaAtual, xPecaAnalisada, yPecaAnalisada):
    pecaAtual = tabuleiro[xPecaAtual][yPecaAtual]
    pecaAnalisada = tabuleiro[xPecaAnalisada][yPecaAnalisada]
    if pecaAtual == '0':
        return 0
    if pecaAtual.isupper():
        if pecaAnalisada.isupper():
            return 1  # caso das duas serem UPPERCASE
        return 0  # caso da atual ser UPPERCASE e a analisada LOWECASE
    if pecaAnalisada.isupper():
        return 0  # caso da atual ser LOWERCASE e a analisada UPPERCASE
    return 1  # caso das duas serem LOWERCASE


def movimento_obrigatorio_torre(tabuleiro, x, y):
    listaPossiveis = []
    i = x + 1
    while (i < len(tabuleiro)):
        listaPossiveis.append([i, y])
        if (tabuleiro[i][y] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, y)):
                listaPossiveis.remove([i, y])
            break
        i += 1
    i = x - 1
    while (i >= 0):
        listaPossiveis.append([i, y])
        if (tabuleiro[i][y] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, y)):
                listaPossiveis.remove([i, y])
            break
        i -= 1
    j = y + 1
    while (j < len(tabuleiro[0])):
        listaPossiveis.append([x, j])
        if (tabuleiro[x][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, x, j)):
                listaPossiveis.remove([x, j])
            break
        j += 1
    j = y - 1
    while (j >= 0):
        listaPossiveis.append([x, j])
        if (tabuleiro[x][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, x, j)):
                listaPossiveis.remove([x, j])
            break
        j -= 1
    return listaPossiveis


def movimento_obrigatorio_bispo(tabuleiro, x, y):
    listaPossiveis = []
    i = x + 1
    j = y + 1
    while (i < len(tabuleiro) and j < len(tabuleiro[0])):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])
            break
        i += 1
        j += 1

    i = x - 1
    j = y - 1
    while (i >= 0 and j >= 0):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])
            break
        i -= 1
        j -= 1

    i = x - 1
    j = y + 1
    while (j < len(tabuleiro[0]) and i >= 0):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])
            break
        j += 1
        i -= 1

    i = x + 1
    j = y - 1
    while (j >= 0 and i < len(tabuleiro)):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])
            break
        j -= 1
        i += 1

    return listaPossiveis


def movimento_obrigatorio_rainha(tabuleiro, x, y):
    movimentosPossiveisBispo = movimento_obrigatorio_bispo(tabuleiro, x, y)
    movimentosPossiveisTorre = movimento_obrigatorio_torre(tabuleiro, x, y)
    listaPossiveisRainha = movimentosPossiveisTorre
    for i in range(len(movimentosPossiveisBispo)):
        listaPossiveisRainha.append(movimentosPossiveisBispo[i])

    return listaPossiveisRainha


def movimento_obrigatorio_rei(tabuleiro, x, y):
    listaPossiveis = []
    i = x + 1
    j = y + 1
    if (i < len(tabuleiro) and j < len(tabuleiro[0])):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x - 1
    j = y - 1
    if (i >= 0 and j >= 0):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x - 1
    j = y + 1
    if (i >= 0 and j < len(tabuleiro[0])):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x + 1
    j = y - 1
    if (i < len(tabuleiro) and j >= 0):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x + 1
    j = y
    if (i < len(tabuleiro)):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x
    j = y + 1
    if (j < len(tabuleiro)):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x - 1
    j = y
    if (i >= 0):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x
    j = y - 1
    if (j >= 0):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    return listaPossiveis


def movimento_obrigatorio_peao(tabuleiro, x, y):
    listaPossiveis = []
    if (tabuleiro[x][y].isupper()):
        i = x + 1
        j = y
        if (i < len(tabuleiro)):
            if (tabuleiro[i][j] == '0'):
                listaPossiveis.append([i, j])
        if (x == 1 and tabuleiro[i][j] == '0' and tabuleiro[i+1][j] == '0'):
            listaPossiveis.append([i + 1, j])
        if (i < len(tabuleiro) and y + 1 < len(tabuleiro[0]) and tabuleiro[i][y + 1] != '0'):
            if (not isPecaAliada(tabuleiro, x, y, i, y + 1)):
                listaPossiveis.append([i, y + 1])
        if (i < len(tabuleiro) and y - 1 >= 0 and tabuleiro[i][y - 1] != '0'):
            if (not isPecaAliada(tabuleiro, x, y, i, y - 1)):
                listaPossiveis.append([i, y - 1])
    else:
        if (tabuleiro[x][y].islower()):
            i = x - 1
            j = y
            if (i < len(tabuleiro)):
                if (tabuleiro[i][j] == '0'):
                    listaPossiveis.append([i, j])
            if (x == 6 and tabuleiro[x - 1][j] == '0' and tabuleiro[x-2][j] == '0'):
                listaPossiveis.append([i - 1, j])
            if (i >= 0 and j + 1 < len(tabuleiro[0]) and tabuleiro[i][j + 1] != '0'):
                if (not isPecaAliada(tabuleiro, x, y, i, j + 1)):
                    listaPossiveis.append([i, j + 1])
            if (i >= 0 and j - 1 >= 0 and tabuleiro[i][j - 1] != '0'):
                if (not isPecaAliada(tabuleiro, x, y, i, j - 1)):
                    listaPossiveis.append([i, j - 1])
    return listaPossiveis


def movimento_obrigatorio_cavalo(tabuleiro, x, y):
    listaPossiveis = []
    i = x + 1
    j = y + 2
    if (i < len(tabuleiro) and j < len(tabuleiro[0])):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x - 1
    j = y - 2
    if (i >= 0 and j >= 0):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x - 1
    j = y + 2
    if (i >= 0 and j < len(tabuleiro[0])):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x + 1
    j = y - 2
    if (i < len(tabuleiro) and j >= 0):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x + 2
    j = y + 1
    if (i < len(tabuleiro) and j < len(tabuleiro[0])):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x - 2
    j = y - 1
    if (i >= 0 and j >= 0):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x - 2
    j = y + 1
    if (i >= 0 and j < len(tabuleiro[0])):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    i = x + 2
    j = y - 1
    if (i < len(tabuleiro) and j >= 0):
        listaPossiveis.append([i, j])
        if (tabuleiro[i][j] != '0'):
            if (isPecaAliada(tabuleiro, x, y, i, j)):
                listaPossiveis.remove([i, j])

    return listaPossiveis


def movimentos_possiveis_peca(tabuleiro, atualX, atualY):
    peca = tabuleiro[atualX][atualY]
    listaPossiveis = []
    if (peca == 'p' or peca == 'P'):
        listaPossiveis = movimento_obrigatorio_peao(tabuleiro, atualX, atualY)
    elif (peca == 'c' or peca == 'C'):
        listaPossiveis = movimento_obrigatorio_cavalo(tabuleiro, atualX, atualY)
    elif (peca == 'r' or peca == 'R'):
        listaPossiveis = movimento_obrigatorio_rei(tabuleiro, atualX, atualY)
    elif (peca == 'a' or peca == 'A'):
        listaPossiveis = movimento_obrigatorio_rainha(tabuleiro, atualX, atualY)
    elif (peca == 'b' or peca == 'B'):
        listaPossiveis = movimento_obrigatorio_bispo(tabuleiro, atualX, atualY)
    elif (peca == 't' or peca == 'T'):
        listaPossiveis = movimento_obrigatorio_torre(tabuleiro, atualX, atualY)
    return listaPossiveis


def analisaSePecaAmeaca(tabuleiro, lista, tipoPeca):
    for posicao in lista:
        if (tabuleiro[posicao[0]][posicao[1]] == tipoPeca):
            return 1
    return 0


def listaMovimentosTodosOsPeoesInimigos(tabuleiro, posRei):
    lista = []
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if (not isPecaAliada(tabuleiro, posRei[0], posRei[1], i, j)):
                if (tabuleiro[i][j] == 'P' or tabuleiro[i][j] == 'p'):
                    for movimento in movimento_obrigatorio_peao(tabuleiro, i, j):
                        lista.append(movimento)
    return lista


def verificaCheckReiPecaBranca(tabuleiro, xPeca, yPeca, xDestino, yDestino):
    peca = tabuleiro[xPeca][yPeca]
    destino = tabuleiro[xDestino][yDestino]
    tabuleiro[xDestino][yDestino] = peca
    tabuleiro[xPeca][yPeca] = '0'
    posReiBranco = []
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == 'r':
                posReiBranco = [i, j]
    # analisandoCavalo
    listaParaAnalise = movimento_obrigatorio_cavalo(tabuleiro, posReiBranco[0], posReiBranco[1])
    if (analisaSePecaAmeaca(tabuleiro, listaParaAnalise, 'C')):
        tabuleiro[xDestino][yDestino] = destino
        tabuleiro[xPeca][yPeca] = peca
        return 1

    # analisandoRainha
    listaParaAnalise = movimento_obrigatorio_rainha(tabuleiro, posReiBranco[0], posReiBranco[1])
    if (analisaSePecaAmeaca(tabuleiro, listaParaAnalise, 'A')):
        tabuleiro[xDestino][yDestino] = destino
        tabuleiro[xPeca][yPeca] = peca
        return 1

    # analisandoBispo
    listaParaAnalise = movimento_obrigatorio_bispo(tabuleiro, posReiBranco[0], posReiBranco[1])
    if (analisaSePecaAmeaca(tabuleiro, listaParaAnalise, 'B')):
        tabuleiro[xDestino][yDestino] = destino
        tabuleiro[xPeca][yPeca] = peca
        return 1

    # analisandoTorre
    listaParaAnalise = movimento_obrigatorio_torre(tabuleiro, posReiBranco[0], posReiBranco[1])
    if (analisaSePecaAmeaca(tabuleiro, listaParaAnalise, 'T')):
        return 1

    # analisandoRei
    listaParaAnalise = movimento_obrigatorio_rei(tabuleiro, posReiBranco[0], posReiBranco[1])
    if (analisaSePecaAmeaca(tabuleiro, listaParaAnalise, 'R')):
        tabuleiro[xDestino][yDestino] = destino
        tabuleiro[xPeca][yPeca] = peca
        return 1

    # analisandoPeao
    listaParaAnalise = listaMovimentosTodosOsPeoesInimigos(tabuleiro, posReiBranco)
    if (analisaSePecaAmeaca(tabuleiro, listaParaAnalise, 'r')):
        tabuleiro[xDestino][yDestino] = destino
        tabuleiro[xPeca][yPeca] = peca
        return 1
    tabuleiro[xDestino][yDestino] = destino
    tabuleiro[xPeca][yPeca] = peca
    return 0


def verificaCheckReiPecaPreta(tabuleiro, xPeca, yPeca, xDestino, yDestino):
    peca = tabuleiro[xPeca][yPeca]
    destino = tabuleiro[xDestino][yDestino]
    tabuleiro[xDestino][yDestino] = peca
    tabuleiro[xPeca][yPeca] = '0'
    posReiPreto = []
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == 'R':
                posReiPreto = [i, j]
    # analisandoCavalo
    listaParaAnalise = movimento_obrigatorio_cavalo(tabuleiro, posReiPreto[0], posReiPreto[1])
    if (analisaSePecaAmeaca(tabuleiro, listaParaAnalise, 'c')):
        tabuleiro[xDestino][yDestino] = destino
        tabuleiro[xPeca][yPeca] = peca
        return 1

    # analisandoRainha
    listaParaAnalise = movimento_obrigatorio_rainha(tabuleiro, posReiPreto[0], posReiPreto[1])
    if (analisaSePecaAmeaca(tabuleiro, listaParaAnalise, 'a')):
        tabuleiro[xDestino][yDestino] = destino
        tabuleiro[xPeca][yPeca] = peca
        return 1

    # analisandoBispo
    listaParaAnalise = movimento_obrigatorio_bispo(tabuleiro, posReiPreto[0], posReiPreto[1])
    if (analisaSePecaAmeaca(tabuleiro, listaParaAnalise, 'b')):
        tabuleiro[xDestino][yDestino] = destino
        tabuleiro[xPeca][yPeca] = peca
        return 1

    # analisandoTorre
    listaParaAnalise = movimento_obrigatorio_torre(tabuleiro, posReiPreto[0], posReiPreto[1])
    if (analisaSePecaAmeaca(tabuleiro, listaParaAnalise, 't')):
        tabuleiro[xDestino][yDestino] = destino
        tabuleiro[xPeca][yPeca] = peca
        return 1

    # analisandoRei
    listaParaAnalise = movimento_obrigatorio_rei(tabuleiro, posReiPreto[0], posReiPreto[1])
    if (analisaSePecaAmeaca(tabuleiro, listaParaAnalise, 'r')):
        tabuleiro[xDestino][yDestino] = destino
        tabuleiro[xPeca][yPeca] = peca
        return 1

    # analisandoPeao
    listaParaAnalise = listaMovimentosTodosOsPeoesInimigos(tabuleiro, posReiPreto)
    if (analisaSePecaAmeaca(tabuleiro, listaParaAnalise, 'R')):
        tabuleiro[xDestino][yDestino] = destino
        tabuleiro[xPeca][yPeca] = peca
        return 1
    tabuleiro[xDestino][yDestino] = destino
    tabuleiro[xPeca][yPeca] = peca
    return 0


def funcao_promocao_Peao(tabuleiro, xPeca, yPeca, pecaPromovida):
    tabuleiro[xPeca][yPeca] = pecaPromovida
    return tabuleiro


def verificaFimDeJogo(tabuleiro, turno):
    for x in range(len(tabuleiro)):
        for y in range(len(tabuleiro[0])):
            if turno % 2 == 0:
                if tabuleiro[x][y].isupper():
                    movimentos = movimentos_possiveis_peca(tabuleiro, x, y);
                    for movimento in movimentos:
                        if (not verificaCheckReiPecaPreta(tabuleiro, x, y, movimento[0], movimento[1])):
                            return 0
            if turno % 2 == 1:
                if not tabuleiro[x][y].isupper():
                    movimentos = movimentos_possiveis_peca(tabuleiro, x, y);
                    for movimento in movimentos:
                        if (not verificaCheckReiPecaBranca(tabuleiro, x, y, movimento[0], movimento[1])):
                            return 0

    return 1
