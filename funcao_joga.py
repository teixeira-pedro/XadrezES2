import movimentos_pecas

def funcao_joga(tabuleiro,atualX,atualY,desejadoX,desejadoY):
    listaPossiveis = movimentos_possiveis_peca(tabuleiro,atualX,atualY)

    if([desejadoX,desejadoY] in listaPossiveis):
        tabuleiro[desejadoX][desejadoY] = tabuleiro[atualX][atualY]
        tabuleiro[atualX][atualY] = '0'

        
