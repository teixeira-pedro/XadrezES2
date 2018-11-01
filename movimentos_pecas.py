def isPecaAliada(tabuleiro,xPecaAtual,yPecaAtual,xPecaAnalisada,yPecaAnalisada):
    pecaAtual = tabuleiro[xPecaAtual][yPecaAtual]
    pecaAnalisada = tabuleiro[xPecaAnalisada][yPecaAnalisada]
    if pecaAtual == '0':
        return false
    if pecaAtual.isupper():
        if pecaAnalisada.isupper():
            return 1  #caso das duas serem UPPERCASE
        return 0  #caso da atual ser UPPERCASE e a analisada LOWECASE
    if pecaAnalisada.isupper():
        return 0  #caso da atual ser LOWERCASE e a analisada UPPERCASE
    return 1  #caso das duas serem LOWERCASE

def movimento_obrigatorio_torre(tabuleiro,x,y):
    listaPossiveis = []
    i=x+1
    while(i < len(tabuleiro)):
        listaPossiveis.append([i,y])
        if (tabuleiro[i][y] !='0'):
            if(isPecaAliada(tabuleiro,x,y,i,y)): 
                listaPossiveis.remove([i,y])
            break
        i+=1
    i = x-1
    while(i>=0):
        listaPossiveis.append([i,y])
        if (tabuleiro[i][y] !='0'):
            if(isPecaAliada(tabuleiro,x,y,i,y)): 
                listaPossiveis.remove([i,y])
            break
        i-=1
    j = y+1
    while(j < len(tabuleiro[0])):
        listaPossiveis.append([x,j])
        if (tabuleiro[x][j] !='0'):
            if(isPecaAliada(tabuleiro,x,y,x,j)): 
                listaPossiveis.remove([x,j])
            break
        j+=1
    j = y-1
    while(j >= 0):
        listaPossiveis.append([x,j])
        if (tabuleiro[x][j] !='0'):
            if(isPecaAliada(tabuleiro,x,y,x,j)): 
                listaPossiveis.remove([x,j])
            break
        j-=1
    return listaPossiveis

def movimento_obrigatorio_bispo(tabuleiro,x,y):
    listaPossiveis = []
    i=x+1
    j=y+1
    while(i < len(tabuleiro) and j < len(tabuleiro[0])):
        listaPossiveis.append([i,j])
        if (tabuleiro[i][j] != '0'):
            if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])
            break
        i+=1
        j+=1
        
    i = x-1
    j = y-1
    while(i>=0 and j>=0):
        listaPossiveis.append([i,j])
        if (tabuleiro[i][j] != '0'):
            if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])
            break
        i-=1
        j-=1

    i = x-1
    j = y+1
    while(j < len(tabuleiro[0]) and i>=0):
        listaPossiveis.append([i,j])
        if (tabuleiro[i][j] != '0'):
            if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])
            break
        j+=1
        i-=1

    i = x+1
    j = y-1
    while(j >= 0 and i <len(tabuleiro)):
        listaPossiveis.append([i,j])
        if (tabuleiro[i][j] != '0'):
            if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])
            break
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

def movimento_obrigatorio_rei(tabuleiro,x,y):
    listaPossiveis = []
    i = x+1
    j = y+1
    if(i<len(tabuleiro) and j<len(tabuleiro[0])):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])

    i = x-1
    j = y-1
    if(i>=0 and j>=0):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])

    i = x-1
    j = y+1
    if(i>=0 and j<len(tabuleiro[0])):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])
    
    i = x+1
    j = y-1
    if(i<len(tabuleiro) and j>=0):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])

    i = x+1
    j = y
    if(i<len(tabuleiro)):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])

    i = x
    j = y+1
    if(j<len(tabuleiro)):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])
        
    i = x-1
    j = y
    if(i>=0):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])

    i = x
    j = y-1
    if(j>=0):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])

    return listaPossiveis

def movimento_obrigatorio_peao(tabuleiro,x,y):
    listaPossiveis = []
    if(tabuleiro[x][y].isupper()):
        i = x+1
        j = y
        if(i<len(tabuleiro)):
            if(tabuleiro[i][j] == '0'):
                listaPossiveis.append([i,j])
        if(x<len(tabuleiro) and y <len(tabuleiro[0]) and tabuleiro[i][j] != '0'):
            if(isPecaAliada(tabuleiro,x,y,x+1,y+1)):
                listaPossiveis.append([i,j])
        if(x<len(tabuleiro) and y >=0 and tabuleiro[i][j] != '0'):
            if(isPecaAliada(tabuleiro,x,y,x+1,y-1)):
                listaPossiveis.append([i,j])
    else:
        if(tabuleiro[x][y].islower()):
            i = x-1
            j = y
            if(i<len(tabuleiro)):
                if(tabuleiro[i][j] == '0'):
                    listaPossiveis.append([i,j])
            if(x>=0 and y <len(tabuleiro[0]) and tabuleiro[i][j] != '0'):
                if(isPecaAliada(tabuleiro,x,y,x+1,y+1)):
                    listaPossiveis.append([i,j])
            if(x>=0 and y >=0 and tabuleiro[i][j] != '0'):
                if(isPecaAliada(tabuleiro,x,y,x+1,y-1)):
                    listaPossiveis.append([i,j])
    return listaPossiveis

def movimento_obrigatorio_cavalo(tabuleiro,x,y):
    listaPossiveis = []
    i = x+1
    j = y+2
    if(i<len(tabuleiro) and j<len(tabuleiro[0])):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])

    i = x-1
    j = y-2
    if(i>=0 and j>=0):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])

    i = x-1
    j = y+2
    if(i>=0 and j<len(tabuleiro[0])):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])
    
    i = x+1
    j = y-2
    if(i<len(tabuleiro) and j>=0):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])
                
    i = x+2
    j = y+1
    if(i<len(tabuleiro) and j<len(tabuleiro[0])):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])

    i = x-2
    j = y-1
    if(i>=0 and j>=0):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])

    i = x-2
    j = y+1
    if(i>=0 and j<len(tabuleiro[0])):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])
    
    i = x+2
    j = y-1
    if(i<len(tabuleiro) and j>=0):
        listaPossiveis.append([i,j])
        if(tabuleiro[i][j] != '0'):
           if(isPecaAliada(tabuleiro,x,y,i,j)): 
                listaPossiveis.remove([i,j])

    return listaPossiveis
