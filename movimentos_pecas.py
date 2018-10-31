def movimento_obrigatorio_torre(tabuleiro,x,y):
    listaPossiveis = []
    i=x+1
    while(i < len(tabuleiro)):
        listaPossiveis.append([i,y])
        i+=1
        if (tabuleiro[i][y] !=0):
            if(isPecaAliada(tabuleiro,x,y,i,y)): #criar a funcao que verifica se a peça é aliada ou não (dados o tabuleiro, posicao da peca atual e peca colisao )
                listaPossiveis.remove([i,y])
                break
    i = x-1
    while(i>=0):
        #Verificar se possui peças na frente
        listaPossiveis.append([i,y])
        i-=1
    
    j = y+1
    while(j < len(tabuleiro)[0]):
        #Verificar se possui peças na frente
        listaPossiveis.append([x,j])
        j+=1
    
    j = y-1
    while(j >= 0):
        #Verificar se possui peças na frente
        listaPossiveis.append([x,j])
        j-=1
    
    return listaPossiveis

def movimento_obrigatorio_bispo(tabuleiro,x,y):
    listaPossiveis = []
    i=x+1
    j=y+1
    while(i < len(tabuleiro) and j < len(tabuleiro)[0]):
        #Verificar se possui peças na frente
        listaPossiveis.append([i,j])
        i+=1
        j+=1
    
    i = x-1
    j = y-1
    while(i>=0 and j>=0):
        #Verificar se possui peças na frente
        listaPossiveis.append([i,j])
        i-=1
        j-=1

    i = x-1
    j = y+1
    while(j < len(tabuleiro)[0] and i>=0):
        #Verificar se possui peças na frente
        listaPossiveis.append([i,j])
        j+=1
        i-=1

    i = x+1
    j = y-1
    while(j >= 0 and i <len(tabuleiro)):
        #Verificar se possui peças na frente
        listaPossiveis.append([i,j])
        j-=1
        i+=1
    
    return listaPossiveis

def movimento_obrigatorio_rainha(tabuleiro,x,y):
    movimentosPossiveisBispo = movimento_obrigatorio_bispo(tabuleiro,x,y)
    movimentosPossiveisTorre = movimento_obrigatorio_torre(tabuleiro,x,y)
    listaPossiveisRainha = movimentosPossiveisTorre
    for i in range(len(movimentosPossiveisBispo)):
        listaPossiveisRainha.append(movimentosPossiveisBispo[i])

    return listaPossiveisRainha 
