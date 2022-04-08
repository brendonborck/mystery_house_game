import pygame
import constantes
from utils import Utils

class Menu():
    def __init__(self, tela, tela_inicio):
        self.tela = tela
        self.tela_inicio = tela_inicio
        self.esta_rodando = True
        self.jogando = False
        self.tamanho_fonte = 35
        self.imagem_jogador = None
        self.velocidade = None


    def mostrar_opcoes(self, cores):
        Utils().mostrar_texto(self.tela, 'Modo 1', self.tamanho_fonte, cores[0], constantes.LARGURA/2, constantes.ALTURA * 0.7)
        Utils().mostrar_texto(self.tela, 'Modo 2', self.tamanho_fonte, cores[1], constantes.LARGURA/2, constantes.ALTURA * 0.8)
        Utils().mostrar_texto(self.tela, 'Modo 3', self.tamanho_fonte, cores[2], constantes.LARGURA/2, constantes.ALTURA * 0.9)
        pygame.display.flip()

    
    def rodar_menu(self):
        num_botoes = 3
        botao_selecionado = 0
        cores = [constantes.PRETO, constantes.BRANCO, constantes.BRANCO]
        self.mostrar_opcoes(cores)

        no_menu=True
        while no_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    no_menu = False
                    self.esta_rodando = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        no_menu = False
                        self.opcoes_de_jogo(botao_selecionado)
                    elif event.key == pygame.K_ESCAPE:
                        no_menu = False
                        self.esta_rodando = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP and botao_selecionado > 0:
                        botao_selecionado -= 1
                    if event.key == pygame.K_DOWN and botao_selecionado < num_botoes - 1:
                        botao_selecionado += 1
                    if event.key in (pygame.K_UP, pygame.K_DOWN):
                        cores = [constantes.BRANCO] * num_botoes
                        cores[botao_selecionado] = constantes.PRETO
        
                        retangulo_tela = self.tela_inicio.get_rect()
                        retangulo_tela.midtop = (constantes.LARGURA/2,0)
                        self.tela.blit(self.tela_inicio, retangulo_tela)
                        self.mostrar_opcoes(cores)
                        pygame.display.update()

    
    def opcoes_de_jogo(self, botao_selecionado):
        if botao_selecionado==0:
            self.imagem_jogador = "player1.png"
            self.velocidade = 10
        elif  botao_selecionado==1:
            self.imagem_jogador = "player2.png"
            self.velocidade = 10
        elif  botao_selecionado==2:
            self.imagem_jogador = "player1.png"
            self.velocidade = 20
