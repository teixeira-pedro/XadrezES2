import pygame
import time
from movimentos_pecas import *
#from movimento_pecas.py import *
import os

pygame.init()


FUNDO=os.getcwd()+'\\imgs\\bg.png'

LARGURA = 640
ALTURA = 640

BEGE = (238,238,210)
PRETO = (0, 0, 0)
FOSCO = (158, 158, 158)
BRANCO = (255, 255, 255)
CINZA = (100, 100, 100)
VERDE_ESCURO = (118,150,86)
YELLOW = (0, 255, 0)
VERMELHO_CLARO = (255, 0, 0)
AZUL = (0, 0, 255)
COR_FUNDO = (54, 54, 54)
COR_TAB = (0, 31, 0)
YELLOW = (255,215,0)
CINZA = (222, 235, 235)
MARROM = (235,199,158)
CORAL = (240,128,128)
VERDE_CLARO = (0, 255, 0)
TAMANHO_QUADRADO = 80
TAMANHO_PEÇA = 80



tela = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()




def movimentos_obrigatorios(casa):
    return None

#toma conta do jogo
class Jogo:
    # a função init é a construtora da classe
        def __init__(self):
            self.estado='jogando'
            #TURNO ÍMPAR = VEZ DAS BRANCAS
            #TURNO PAR = VEZ DAS PRETAS
            self.turno=1
            self.casa_selecionada=[]
            self.jogadores=('j','J')
            #CAPS LOCK : PRETO ; sem caps lock : branco
            # T : torre
            # C : cavalo
            # B : bispo
            # A : rainha
            # R : rei
            # P : peão
            self.tabuleiro=[
                            ['T','C','B','A','R','B','C','T'],
                            ['P','P','P','P','P','P','P','P'],
                            ['0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0'],
                            ['p','p','p','p','p','p','p','p'],
                            ['t','c','b','r','a','b','c','t'],
            ]

        def funcao_joga(self,atualX,atualY,desejadoX,desejadoY):
            listaPossiveis = movimentos_possiveis_peca(self.tabuleiro,atualX,atualY)
            moveu = 0
            if([desejadoX,desejadoY] in listaPossiveis):
                if(isPreta(self.tabuleiro,atualX,atualY)):
                    if(verificaCheckReiPecaPreta(self.tabuleiro,atualX,atualY,desejadoX,desejadoY)):
                        print ("Check no Rei Preto RollBack")
                        return moveu
                else:
                    if(verificaCheckReiPecaBranca(self.tabuleiro, atualX, atualY, desejadoX, desejadoY)):
                        print("check no Rei Branco RollBack")
                        return moveu
                self.tabuleiro[desejadoX][desejadoY] = self.tabuleiro[atualX][atualY]
                self.tabuleiro[atualX][atualY] = '0'
                moveu  =1
            return moveu
        def set_tabuleiro(self,novo):
            self.tabuleiro=novo
        def get_tabuleiro(self):
            return self.tabuleiro
        def get_peca(self,xy):
            return self.get_tabuleiro()[xy[0]][xy[1]]
        def get_turno(self):
            return self.turno
        def eh_vez_das_pretas(self):
            return 0==self.turno%2
        def eh_vez_das_brancas(self):
            return not self.eh_vez_das_pretas()
        def pixels_2_tabuleiro(self,pygameobj):
            return (int((pygameobj.get_pos()[0])/80),int((pygameobj.get_pos()[1])/80))
        def get_pecas_restantes(self,jogador):            
            CONT_PRETA=0
            cont_branca=0
            for linha in self.tabuleiro:
                for item in linha:
                    if item.isupper() :
                        CONT_PRETA=CONT_PRETA+1
                    if item.islower() :
                        cont_branca=cont_branca+1
            if jogador.isupper(): # se é preta
                return CONT_PRETA
            if jogador.islower(): # se é branca
                return cont_branca
            return 0
        def coloca_peca(self,i,j,peca):
            self.tabuleiro[i][j]=peca
        def retira_peca(self,i,j):
            self.tabuleiro[i][j]='0'
        #muda a vez da jogada
        def gira_turno(self):
            self.turno=self.turno+1
        #realiza a promoção de peças, dada a posicao da peça atual e
        #a nova desehada
        def promove(self,i,j,nova):
            # não vale promover pra peão ou rei
            if (nova!='p' and nova!='r' and nova!='P' and nova!='R'):
            #só peões na ultima casa podem ser promovidos 
                if self.tabuleiro[i][j]=='p' and i==0:
                    self.tabuleiro[i][j]=nova.lower()
                if self.tabuleiro[i][j]=='P' and i==7:                
                    self.tabuleiro[i][j]=nova.upper()
        # converte a posição da matriz em pixels para serem exibidos
        def tabuleiro_2_pixels(self,i,j):
            return [(80*i,80*j),((80*i)+80,(80*j)+j)]
        def ganhou(self):
            #xeque mate ?????
            return 0
        #pega o endereco do png da peça
        def imagem_peca(self,peca):
            if peca=='p':
                return os.getcwd()+'\\imgs\\peao_branco.png'                
            if peca=='P':
                return os.getcwd()+'\\imgs\\peao_preto.png'                
            if peca=='r':
                return os.getcwd()+'\\imgs\\rei_branco.png'                
            if peca=='R':
                return os.getcwd()+'\\imgs\\rei_preto.png'                
            if peca=='a':
                return os.getcwd()+'\\imgs\\rainha_branco.png'                
            if peca=='A':
                return os.getcwd()+'\\imgs\\rainha_preto.png'                
            if peca=='t':
                return os.getcwd()+'\\imgs\\torre_branco.png'                
            if peca=='T':
                return os.getcwd()+'\\imgs\\torre_preto.png'                
            if peca=='b':
                return os.getcwd()+'\\imgs\\bispo_branco.png'                
            if peca=='B':
                return os.getcwd()+'\\imgs\\bispo_preto.png'                
            if peca=='c':
                return os.getcwd()+'\\imgs\\cavalo_branco.png'                
            if peca=='C':
                return os.getcwd()+'\\imgs\\cavalo_preto.png'

        def desenha(self):
            matriz=[]
            #desenhando fundo
            bg=pygame.image.load(FUNDO)
            tela.blit(bg,(0,0))
            #desenhando pecas
            for i in range(len(self.get_tabuleiro())):
                for j in range(len(self.get_tabuleiro()[i])):
                    if self.imagem_peca(self.get_tabuleiro()[i][j]) :
                        peca=pygame.image.load(self.imagem_peca(self.get_tabuleiro()[i][j]))
                        tela.blit(peca,self.tabuleiro_2_pixels(j,i)[0])
def loop_jogo():
    sair = False

    
    org=[]
    
    jogo=Jogo()
    while not sair:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair = True
                pygame.quit()
                quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if int(str(evento.button)) == 1 and org == []:
                    selecao_orig=jogo.pixels_2_tabuleiro(pygame.mouse)
                    print("selecionado:", selecao_orig, [selecao_orig[1], selecao_orig[0]])
                    peca_orig = jogo.get_peca([selecao_orig[1], selecao_orig[0]])
                    if peca_orig != '0':
                        print('selecionei')
                        org=selecao_orig
                    break
                print(jogo.tabuleiro)
                print("org:", org)
                if int(str(evento.button)) == 1 and org != []:
                    selecao = jogo.pixels_2_tabuleiro(pygame.mouse)
                    print("selecionado:", selecao, jogo.get_tabuleiro()[selecao[1]][selecao[0]])
                    print('joga')
                    jogo.funcao_joga(org[1], org[0], selecao[1], selecao[0])
                    org = []
                    print(jogo.tabuleiro)
                    break
        tela.fill(PRETO)
        jogo.desenha()
        pygame.display.update()
        clock.tick(60)
loop_jogo()
pygame.quit()
quit()
