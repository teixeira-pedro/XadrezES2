import pygame
import time
from movimentos_pecas import *
# from movimento_pecas.py import *
import os
import platform
from math import sqrt
from random import randint
import sys
from tkinter import *

pygame.init()


# como utilizar essa janela no meio da promoção???
def pega_promocao():
    return e1.get()


def tela_promocao():
    master = Tk()
    Label(master, text='inisra a seguir para qual peça promover:').grid(row=0)
    Label(master, text='[R]ainha, [B]ispo, [T]orre, [C]avalo').grid(row=1)
    e1 = Entry(master)
    e1.grid(row=1, column=1)
    Button(master, text='Confirma', command=pega_promocao).grid(row=3, column=1, sticky=W, pady=4)
    master.quit()


def casa_aleatoria():
    return [randint(0, 7), randint(0, 7)]


FUNDO = os.getcwd() + '\\imgs\\bg.png'
FUNDO_LINUX_MAC_OSX = FUNDO.replace('\\', '/')

LARGURA = 640
ALTURA = 640

BEGE = (238, 238, 210)
PRETO = (0, 0, 0)
FOSCO = (158, 158, 158)
BRANCO = (255, 255, 255)
CINZA = (100, 100, 100)
VERDE_ESCURO = (118, 150, 86)
YELLOW = (0, 255, 0)
VERMELHO_CLARO = (255, 0, 0)
AZUL = (0, 0, 255)
COR_FUNDO = (54, 54, 54)
COR_TAB = (0, 31, 0)
YELLOW = (255, 215, 0)
CINZA = (222, 235, 235)
MARROM = (235, 199, 158)
CORAL = (240, 128, 128)
VERDE_CLARO = (0, 255, 0)
TAMANHO_QUADRADO = 80
TAMANHO_PEÇA = 80
AMARELO_HIGHLIGHT = (255, 215, 0)

INFINITO = float("inf")

tela = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()


# funcao auxiliar
def in_matriz(proc, m):
    for linha in m:
        if proc in linha:
            return True
    return False


def convert_platform(estado):
    if platform.system().lower() != 'windows':
        return estado.replace('\\', '/')
    else:
        return estado


# ------------------------------------------------------funções da IA--------------------------------------

# UTILITY, FUNÇÃO QUE DIZ QUEM ESTÁ "MELHOR" NO JOGO :
#       valores tendendo à + infinito : PRETAS se dando bem
#       valores tendendo à - infinito : as brancas
#       0 : equilibrio de jogo

# Foram utilizados três critérios a ponderar : quantidade de peças,
#                                             peso de cada peça
#                                             proximidade de cada peça em relação ao rei inimigo

# assim, a "pontuação" de cada lado é dada pela soma de todas as peças do jogo vezes os pesos relacionados
# é extraido a "pontuação" de cada lado, e se subtrai, a diferença diz quem ta melhor no jogo (+ PRETAS) (- BRANCAS) (0 EQUILIBRIO)

# pesos : P = 1  ; P (perto da casa de promoção (nas casas 4,5 ou 6) ) = 4
#        C = 5  ; T ou B = 10 ;  A (rainha) = 16 ; R = 20

def UTILITY(T):
    pesoP = 0
    pesoB = 0
    for i in range(len(T)):
        for j in range(len(T[i])):
            pesoB += (DPRA([i, j], localiza_rei_adversario(T, 'r')) * (
                    (1 * 'p' == T[i][j]) + (4 * ('p' == T[i][j] and i in [4, 5, 6])) + (5 * 'c' == T[i][j]) + (
                        10 * ((T[i][j] == 't') or (T[i][j] == 'b'))) +
                    (16 * ('a' == T[i][j])) + (20 * ('r' == T[i][j]))
            )
                      )
            pesoB += (DPRA([i, j], localiza_rei_adversario(T, 'R')) * (
                    (1 * 'P' == T[i][j]) + (4 * ('P' == T[i][j] and i in [4, 5, 6])) + (5 * 'C' == T[i][j]) + (
                        10 * ((T[i][j] == 'T') or (T[i][j] == 'B'))) +
                    (16 * ('A' == T[i][j])) + (20 * ('R' == T[i][j]))
            )
                      )
    return pesoP - pesoB


# funcao auxiliar DPRA "Distancia Para Rei Adversario" calcula a distancia pro rei adversario

def DPRA(p, RA):
    return sqrt((abs(RA[0] - p[0]) ** 2) + (abs(RA[1] - p[1]) ** 2))


# funcao auxiliar localiza rei adversario, o nome já explica.

def localiza_rei_adversario(T, rei_jogador_atual):
    for i in range(len(T)):
        for j in range(len(T[i])):
            if rei_jogador_atual == 'r' and T[i][j] == 'R':
                return [i, j]
            if rei_jogador_atual == 'R' and T[i][j] == 'r':
                return [i, j]


# MIN-MAX-Decisão(tabuleiro)

# seria "a" uma ação ? isto é, uma jogada

# tomara a decisao apos calcular as possibilidades de perda ou ganho de uma jogada aleatoria
def MIN_MAX_Decisao(tabuleiro):  # como decidir?
    return i_999(MIN_VALOR(RESULTADO(tabuleiro, a)))


def MAX_VALUE(tabuleiro):
    if TEST_ENC(tabuleiro):
        return UTILITY(tabuleiro)
    V = 0 - INFINITO
    for A in ACOES(tabuleiro):
        v = max(v, MIN_VALUE(RESULTADO(tabuleiro, A)))
    return V


def MIN_VALUE(estado):
    if TEST_ENC(estado):
        return UTILITY(estado)
    v = INFINITO
    for acao in ACOES(estado):
        v = min(v, MAX_VALUE(RESULTADO(estado, acao)))


# aleatoriamente o pc selecionará uma peça e retornara a as ações disponiveis para a peca
def ACOES(T):
    pretas=pega_pecas_pretas(T)
    acoes=[]
    for P in pretas:
        M=movimentos_possiveis_peca(T,P[0],P[1])
        acoes.append(P[0],P[1],M[0],M[1])
    return acoes

# -------------------------------------------------------funções da IA--------------------------------------


def eh_preta(tabuleiro, i, j):
    return tabuleiro[i][j].isupper() and (not eh_vazio(tabuleiro, i, j))


def eh_branca(tabuleiro, i, j):
    return tabuleiro[i][j].islower() and (not eh_vazio(tabuleiro, i, j))


def eh_vazio(tabuleiro, i, j):
    return tabuleiro[i][j] == '0'


def ja_acabou_pecas_restantes_possiveis(pecas_restantes):
    for peca in pecas_restantes:
        if peca[2] == False:
            return False
    return True


def movimentos_obrigatorios(casa):
    return None


def pega_pecas_pretas_old(T):
    novo = []
    for i in range(len(T)):
        for j in range(len(T[i])):
            if eh_preta(T, i, j):
                novo.append([i, j, False])
    return novo


def pega_jogada_aleatoria(pretas, T):
    # print(pretas,'******')
    peca_aleat = []
    jogadas = []
    while jogadas == []:
        ind_aleat = randint(0, len(pretas) - 1)
        peca_aleat = pretas[ind_aleat]
        # print(pretas,'******',peca_aleat)
        jogadas = movimentos_possiveis_peca(T, peca_aleat[0], peca_aleat[1])
    print(jogadas)
    print(peca_aleat)
    ind_aleat = randint(0, len(jogadas) - 1)
    jogada_aleat = jogadas[ind_aleat]
    print(jogada_aleat)
    return [peca_aleat[0], peca_aleat[1], jogada_aleat[0], jogada_aleat[1]]


def pega_pecas_pretas(T):
    novo = []
    for i in range(len(T)):
        for j in range(len(T[i])):
            if eh_preta(T, i, j):
                novo.append([i, j])
    return novo


def pega_jogada_aleatoria_old(pretas, T):
    ind_aleat = randint(0, len(pretas) - 1)
    peca_aleat = pretas[ind_aleat]
    pretas[ind_aleat][2] = True
    achou_jogadas_nao_vazias = False
    while (not ja_acabou_pecas_restantes_possiveis(pretas)) or (not achou_jogadas_nao_vazias):
        jogadas = movimentos_possiveis_peca(T, peca_aleat[0], peca_aleat[1])
        if jogadas != []:
            achou_jogadas_nao_vazias = True
        ind_aleat = randint(0, len(pretas) - 1)
        peca_aleat = pretas[ind_aleat]
        pretas[ind_aleat][2] = True
    if ja_acabou_pecas_restantes_possiveis(pretas) or achou_jogadas_nao_vazias:
        return []
    ind_aleat_jogada = randint(0, len(jogadas) - 1)
    jogada_aleat = jogadas[ind_aleat_jogada]

    return [peca_aleat[0], peca_aleat[1], jogada_aleat[0], jogada_aleat[1]]


# toma conta do jogo
class Jogo:

    # a função init é a construtora da classe
    def __init__(self):
        self.estado = 'jogando'
        # TURNO ÍMPAR = VEZ DAS BRANCAS
        # TURNO PAR = VEZ DAS PRETAS
        self.turno = 1
        self.casa_selecionada = []
        self.jogadores = ('j', 'J')
        self.estado_xeque = ''
        # 'XP' (xeque preto) 'XB' (xeque branco)
        # CAPS LOCK : PRETO ; sem caps lock : branco
        # T : torre
        # C : cavalo
        # B : bispo
        # A : rainha
        # R : rei
        # P : peão
        self.tabuleiro = [
            ['T', 'C', 'B', 'R', 'A', 'B', 'C', 'T'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['t', 'c', 'b', 'r', 'a', 'b', 'c', 't'],
        ]

    def highlights_movimentos_possiveis(self, movs):
        for casa in movs:
            highlight = pygame.image.load(convert_platform(os.getcwd() + '\\imgs\\highlight_verde.png'))
            tela.blit(highlight, self.tabuleiro_2_pixels(casa[0], casa[1])[0])

    def funcao_joga_IA(self):
        pretas = pega_pecas_pretas(self.get_tabuleiro())
        jogada = pega_jogada_aleatoria(pretas, self.get_tabuleiro())
        # print('pretas',pretas,'jogada',jogada)
        atualX = -jogada[0]
        atualY = -jogada[1]
        desejadoX = jogada[2]
        desejadoY = jogada[3]
        # listaPossiveis = movimentos_possiveis_peca(self.tabuleiro, atualX, atualY)

        moveu = 0

        # if ([desejadoX, desejadoY] in listaPossiveis):
        # if (isPreta(self.tabuleiro, atualX, atualY)):
        if (verificaCheckReiPecaPreta(self.tabuleiro, atualX, atualY, desejadoX, desejadoY)):
            print("Check no Rei Preto RollBack")
            print('movimentos possiveis *******', listaPossiveis)

            self.estado_xeque = 'XP'
            return moveu
        else:
            self.estado_xeque = ''
            # else:
            #    if (verificaCheckReiPecaBranca(self.tabuleiro, atualX, atualY, desejadoX, desejadoY)):
            #        print("check no Rei Branco RollBack")
            #        print('movimentos possiveis *******', listaPossiveis)
            #        self.estado_xeque = 'XB'
            #        return moveu
            #    else:
            #        self.estado_xeque = ''
        self.tabuleiro[desejadoX][desejadoY] = self.tabuleiro[atualX][atualY]
        if (self.tabuleiro[desejadoX][desejadoY] == 'P' and desejadoX == len(self.tabuleiro[0]) - 1):
            funcao_promocao_Peao(self.tabuleiro, desejadoX, desejadoY, 'A')
        # elif (self.tabuleiro[desejadoX][desejadoY] == 'p' and desejadoX == 0):
        # funcao_promocao_Peao(self.tabuleiro, desejadoX, desejadoY, 'a')
        self.tabuleiro[atualX][atualY] = '0'
        moveu = 1
        return moveu

    def funcao_joga(self, atualX, atualY, desejadoX, desejadoY):
        listaPossiveis = movimentos_possiveis_peca(self.tabuleiro, atualX, atualY)
        moveu = 0

        if ([desejadoX, desejadoY] in listaPossiveis):
            if (isPreta(self.tabuleiro, atualX, atualY)):
                if (verificaCheckReiPecaPreta(self.tabuleiro, atualX, atualY, desejadoX, desejadoY)):
                    print("Check no Rei Preto RollBack")
                    print('movimentos possiveis *******', listaPossiveis)

                    self.estado_xeque = 'XP'
                    return moveu
                else:
                    self.estado_xeque = ''
            else:
                if (verificaCheckReiPecaBranca(self.tabuleiro, atualX, atualY, desejadoX, desejadoY)):
                    print("check no Rei Branco RollBack")
                    print('movimentos possiveis *******', listaPossiveis)
                    self.estado_xeque = 'XB'
                    return moveu
                else:
                    self.estado_xeque = ''
            self.tabuleiro[desejadoX][desejadoY] = self.tabuleiro[atualX][atualY]
            if (self.tabuleiro[desejadoX][desejadoY] == 'P' and desejadoX == len(self.tabuleiro[0]) - 1):
                funcao_promocao_Peao(self.tabuleiro, desejadoX, desejadoY, 'A')
            elif (self.tabuleiro[desejadoX][desejadoY] == 'p' and desejadoX == 0):
                funcao_promocao_Peao(self.tabuleiro, desejadoX, desejadoY, 'a')
            self.tabuleiro[atualX][atualY] = '0'
            moveu = 1
        return moveu

    def set_tabuleiro(self, novo):
        self.tabuleiro = novo

    def get_tabuleiro(self):
        return self.tabuleiro

    def get_peca(self, xy):
        return self.get_tabuleiro()[xy[0]][xy[1]]

    def get_turno(self):
        return self.turno

    def eh_vez_das_pretas(self):
        return 0 == self.turno % 2

    def eh_vez_das_brancas(self):
        return not self.eh_vez_das_pretas()

    def pixels_2_tabuleiro(self, pygameobj):
        return (int((pygameobj.get_pos()[0]) / 80), int((pygameobj.get_pos()[1]) / 80))

    def get_pecas_restantes(self, jogador):
        CONT_PRETA = 0
        cont_branca = 0
        for linha in self.tabuleiro:
            for item in linha:
                if item.isupper():
                    CONT_PRETA = CONT_PRETA + 1
                if item.islower():
                    cont_branca = cont_branca + 1
        if jogador.isupper():  # se é preta
            return CONT_PRETA
        if jogador.islower():  # se é branca
            return cont_branca
        return 0

    def coloca_peca(self, i, j, peca):
        self.tabuleiro[i][j] = peca

    def retira_peca(self, i, j):
        self.tabuleiro[i][j] = '0'

    # muda a vez da jogada
    def gira_turno(self):
        self.turno = self.turno + 1

    # realiza a promoção de peças, dada a posicao da peça atual e
    # a nova desehada
    def promocao(self):
        for i in range(len(self.tabuleiro)):
            for j in range(len(self.tabuleiro[i])):
                if self.tabuleiro[i][j] == 'p' and 0 == i:
                    self.tabuleiro[i][j] = 'a'  # vira rainha
                if self.tabuleiro[i][j] == 'P' and i == 7:
                    self.tabuleiro[i][j] = 'A'  # vira rainha

    def promove(self, i, j, nova):
        # não vale promover pra peão ou rei
        if (nova != 'p' and nova != 'r' and nova != 'P' and nova != 'R'):
            # só peões na ultima casa podem ser promovidos
            if self.tabuleiro[i][j] == 'p' and i == 0:
                self.tabuleiro[i][j] = nova.lower()
            if self.tabuleiro[i][j] == 'P' and i == 7:
                self.tabuleiro[i][j] = nova.upper()

    # converte a posição da matriz em pixels para serem exibidos
    def tabuleiro_2_pixels(self, i, j):
        return [(80 * i, 80 * j), ((80 * i) + 80, (80 * j) + j)]

    def ganhou(self):
        if not in_matriz('r', self.get_tabuleiro()):
            return 'P'
        elif not in_matriz('R', self.get_tabuleiro()):
            return 'b'
        elif self.empatou():
            return 'e'
        else:
            return None

    def empatou(self):
        T = self.get_tabuleiro()
        # se só houver zeros e os reis, empatou
        # isto é, se a qtd de casas vazias (zero) é 62 e há dois reis
        cont = 0
        reis = 0
        for i in range(len(T)):
            for j in range(len(T[i])):
                if T[i][j] == '0':
                    cont = cont + 1
                if T[i][j].lower() == 'r':
                    reis = reis + 1
        return (cont == 62) and (reis == 2)

        return 0

    # pega o endereco do png da peça

    def imagem_peca_Linux_MacOS(self, peca):
        peca = self.imagem_peca(peca)
        if peca == None:
            return
        else:
            return peca.replace('\\', '/')

    def imagem_peca(self, peca):
        if peca == 'p':
            return os.getcwd() + '\\imgs\\peao_branco.png'
        if peca == 'P':
            return os.getcwd() + '\\imgs\\peao_preto.png'
        if peca == 'r':
            return os.getcwd() + '\\imgs\\rei_branco.png'
        if peca == 'R':
            return os.getcwd() + '\\imgs\\rei_preto.png'
        if peca == 'a':
            return os.getcwd() + '\\imgs\\rainha_branco.png'
        if peca == 'A':
            return os.getcwd() + '\\imgs\\rainha_preto.png'
        if peca == 't':
            return os.getcwd() + '\\imgs\\torre_branco.png'
        if peca == 'T':
            return os.getcwd() + '\\imgs\\torre_preto.png'
        if peca == 'b':
            return os.getcwd() + '\\imgs\\bispo_branco.png'
        if peca == 'B':
            return os.getcwd() + '\\imgs\\bispo_preto.png'
        if peca == 'c':
            return os.getcwd() + '\\imgs\\cavalo_branco.png'
        if peca == 'C':
            return os.getcwd() + '\\imgs\\cavalo_preto.png'

    # desenha(peça selecionada,jogo.ganhou())

    def desenha(self, selecionado):
        # if venceu=='P':
        #    bg=pygame.image.load(convert_platform(os.getcwd()+'\\imgs\\bg_ganhou_P.png'))
        #    tela.blit(bg,(0,0))
        ##    clock.tick(10)
        #   pygame.quit()
        #   quit()
        # elif venceu=='b':
        #    bg=pygame.image.load(convert_platform(os.getcwd()+'\\imgs\\bg_ganhou_b.png'))
        #    tela.blit(bg,(0,0))
        #    clock.tick(10)
        #    quit()
        # elif venceu=='e':
        #   bg=pygame.image.load(convert_platform(os.getcwd()+'\\imgs\\bg_empate.png'))
        #   tela.blit(bg,(0,0))
        #    clock.tick(10)
        #    pygame.quit()
        #    quit()
        # else:
        matriz = []
        # desenhando fundo
        # bg=pygame.image.load(FUNDO_LINUX_MAC_OSX)
        bg = pygame.image.load(convert_platform(FUNDO))  ############
        tela.blit(bg, (0, 0))
        # DESENHANDO HIGHLIGHT
        k = None  ###############QUEM É SELECIONADO? É selecao_orig CHAMAR NORMALMENTE TESTAR

        if selecionado:
            highlight = pygame.image.load(convert_platform(os.getcwd() + '\\imgs\\highlight.png'))
            tela.blit(highlight, self.tabuleiro_2_pixels(selecionado[0], selecionado[1])[0])
            possiveis =  movimentos_possiveis_peca(self.tabuleiro,selecionado[1],selecionado[0])
            for mov in possiveis:
                highlight = pygame.image.load(convert_platform(os.getcwd() + '\\imgs\\highlight_verde.png'))
                tela.blit(highlight, self.tabuleiro_2_pixels(mov[1], mov[0])[0])
        for i in range(len(self.get_tabuleiro())):
            for j in range(len(self.get_tabuleiro()[i])):
                #                    if self.imagem_peca_Linux_MacOS(self.get_tabuleiro()[i][j]) :
                if self.imagem_peca(self.get_tabuleiro()[i][j]):  ##########################
                    peca = pygame.image.load(
                        convert_platform(self.imagem_peca(self.get_tabuleiro()[i][j])))  ##################
                    #                        peca=pygame.image.load(self.imagem_peca_Linux_MacOS(self.get_tabuleiro()[i][j]))
                    tela.blit(peca, self.tabuleiro_2_pixels(j, i)[0])


def jogada_IA_nivel_0(jogo):  # abandonada
    pecas_restantes = []
    T = jogo.get_tabuleiro()
    for i in range(len(T)):
        for j in range(len(T[i])):
            if eh_preta(T, i, j):
                # False : Marcação de que já foi lido pelo verificador da IA
                pecas_restantes.append([i, j, False])

    id_peca = randint(0, len(pecas_restantes) - 1)
    c_aleat = pecas_restantes[id_peca]
    pecas_restantes[id_peca][2] = True
    listaPossiveis = []
    while listaPossiveis != [] or (not ja_acabou_pecas_restantes_possiveis(pecas_restantes)):
        listaPossiveis = movimentos_possiveis_peca(jogo.tabuleiro, c_aleat[0], c_aleat[1])
        id_peca = randint(0, len(pecas_restantes) - 1)
        c_aleat = pecas_restantes[id_peca]
        pecas_restantes[id_peca][2] = True
    if (ja_acabou_pecas_restantes_possiveis(pecas_restantes)):
        return 0
        # nao ha movimentos possiveis, dentre as pecas selecionadas
        # senao, foi selecionado uma lista com movimentos possiveis de uma peca
        # c_aleat guarda a peca e lista_possiveis, as jogadas dessa peca possiveis
    id_jogada = randint(0, len(listaPossiveis) - 1)
    desejado = listaPossiveis[id_jogada]
    moveu = 0
    # if ([desejadoX, desejadoY] in listaPossiveis):
    # if (isPreta(self.tabuleiro, atualX, atualY)):
    if (verificaCheckReiPecaPreta(self.tabuleiro, c_aleat[0], c_aleat[1], desejado[0], desejado[1])):
        print("Check no Rei Preto RollBack")
        print('movimentos possiveis *******', listaPossiveis)
        jogo.estado_xeque = 'XP'
        return moveu
    else:
        jogo.estado_xeque = ''
    jogo.tabuleiro[desejado[0][desejado[1]]] = jogo.tabuleiro[c_aleat[0]][c_aleat[1]]
    if (jogo.tabuleiro[desejado[0][desejado[1]]] == 'P' and desejado[1] == len(jogo.tabuleiro[0]) - 1):
        funcao_promocao_Peao(jogo.tabuleiro, desejado[0], desejado[1], 'A')
    self.tabuleiro[c_aleat[0]][c_aleat[1]] = '0'
    moveu = 1
    return moveu


def loop_jogo():
    sair = False

    vencedor = None
    jogada = []
    org = []
    # selecionado=
    jogo = Jogo()
    while not sair:
        if (verificaFimDeJogo(jogo.tabuleiro, jogo.turno)):
            print(jogo.get_turno())
            tela2 = pygame.display.set_mode((640, 640))
            if (jogo.get_turno() % 2 == 0):
                # vencedor='p'
                vencedor = convert_platform(os.getcwd() + '\\imgs\\bg_ganhou_b.png')
                # bg = pygame.image.load(convert_platform(os.getcwd() + '\\imgs\\bg_ganhou_p.png'))
                # tela2.blit(bg, (0, 0))
                # time.sleep(5)
                # jogo.desenha([],'P')
            if (jogo.get_turno() % 2 == 1):
                vencedor = convert_platform(os.getcwd() + '\\imgs\\bg_ganhou_P.png')
                # vencedor ='b'
                # bg = pygame.image.load(convert_platform(os.getcwd() + '\\imgs\\bg_ganhou_b.png'))
                # tela2.blit(bg, (0, 0))
                # time.sleep(5)
                # jogo.desenha([],'b')
            # turno ímpar e acabou o jogo : preto ganhou
            # turno par e acabou o jogo: branco ganhou
            print('xeque mate')
            print(jogo.estado_xeque)
            sair = True
        if jogo.turno % 2 == 0:
            pretas = pega_pecas_pretas(jogo.get_tabuleiro())
            jogada = pega_jogada_aleatoria(pretas, jogo.get_tabuleiro())
            pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair = True
                pygame.quit()
                quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if (jogada == []):
                    if int(str(evento.button)) == 1 and org == []:
                        selecao_orig = jogo.pixels_2_tabuleiro(pygame.mouse)
                        if (jogo.turno % 2 == 1 and jogo.tabuleiro[selecao_orig[1]][selecao_orig[
                            0]].islower()):  # or (jogo.turno % 2 == 0 and jogo.tabuleiro[selecao_orig[1]][selecao_orig[0]].isupper()):
                            print('VEZ DAS PRETAS')
                            print("selecionado:", selecao_orig, [selecao_orig[1], selecao_orig[0]])
                            peca_orig = jogo.get_peca([selecao_orig[1], selecao_orig[0]])
                            if peca_orig != '0':
                                print('selecionei')
                                org = selecao_orig
                            break
                    print(jogo.tabuleiro)
                    print("org:", org)
                    if int(str(evento.button)) == 1 and org != []:
                        selecao = jogo.pixels_2_tabuleiro(pygame.mouse)
                        print("selecionado:", selecao, jogo.get_tabuleiro()[selecao[1]][selecao[0]])
                        print('joga')
                        if (jogo.funcao_joga(org[1], org[0], selecao[1], selecao[0])):
                            jogo.turno += 1
                        org = []
                        print(jogo.tabuleiro)
                        break
                else:
                    if(jogo.turno %2 == 0):
                        if (jogo.funcao_joga(jogada[0], jogada[1], jogada[2], jogada[3])):
                            jogo.turno += 1
                            jogada = []
                            break
        # tela.fill(PRETO)
        # if vencedor != '':

        #   pygame.time.wait(5000)
        jogo.promocao()  # LISTENER VERIFICANDO SE ALGUEM É APTO A PROMOÇÃO
        jogo.desenha(org)  #
        ####CHAMANDO IA

        pygame.display.update()
        clock.tick()
    return vencedor


img_fim = loop_jogo()
pygame.quit()
if img_fim != None:
    pygame.init()
    tela2 = pygame.display.set_mode((640, 640))
    clock = pygame.time.Clock()
    bg = pygame.image.load(img_fim)
    tela2.blit(bg, [0, 0])
    pygame.display.update()
    pygame.time.wait(5000)
    pygame.quit()
quit()
