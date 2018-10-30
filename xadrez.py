import pygame
import time
from movimento-pecas import *
pygame.init()

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
                            ['t','c','b','a','r','b','c','t'],
            ]
        def get_tabuleiro(self):
            return self.tabuleiro
        def get_turno(self):
            return self.turno
        def eh_vez_das_pretas(self):
            return 0==self.turno%2
        def eh_vez_das_brancas(self):
            return not self.eh_vez_das_pretas()
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
            return [[80*i,80*j],[(80*i)+80,(80*j)+j]]
        def ganhou(self):
            #xeque mate ?????
            return 0
        #pega o endereco do png da peça
        def imagem_peca(self,peca):
            if peca=='p':
                return 'imgs\peao_branco.png'                
            if peca=='P':
                return 'imgs\peao_preto.png'                
            if peca=='r':
                return 'imgs\rei_branco.png'                
            if peca=='R':
                return 'imgs\rei_preto.png'                
            if peca=='a':
                return 'imgs\rainha_branco.png'                
            if peca=='A':
                return 'imgs\rainha_preto.png'                
            if peca=='t':
                return 'imgs\torre_branco.png'                
            if peca=='T':
                return 'imgs\torre_preto.png'                
            if peca=='b':
                return 'imgs\bispo_branco.png'                
            if peca=='B':
                return 'imgs\bispo_preto.png'                
            if peca=='c':
                return 'imgs\cavalo_branco.png'                
            if peca=='C':
                return 'imgs\cavalo_preto.png'

        def desenha(self):
            matriz=[]
            for i in range(8):
                if i%2 == 0:
                    matriz.append(['#', '-', '#', '-', '#', '-', '#', '-'])
                else:
                    matriz.append(['-', '#', '-', '#', '-', '#', '-', '#'])
            y=0
            for l in range(len(matriz)):
                x=0
                for c in range(len(matriz[l])):
                    if matriz[l][c]=='#':
                        pygame.draw.rect(tela, VERDE_ESCURO, (x, y, TAMANHO_QUADRADO, TAMANHO_QUADRADO))
                    else:
                        pygame.draw.rect(tela, BEGE, (x, y, TAMANHO_QUADRADO, TAMANHO_QUADRADO))
                    x += TAMANHO_QUADRADO
                y += TAMANHO_QUADRADO

                




def loop_jogo():
    sair = False

    jogo=Jogo()

    while not sair:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair = True
                pygame.quit()
                quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                jogo.jogadas(pygame.mouse.get_pos())

        tela.fill(PRETO)
        jogo.desenha()

        pygame.display.update()
        clock.tick(60)
        
        
        
loop_jogo()
pygame.quit()
quit()
