import pygame
import constantes
from menu import Menu
from personagem import Personagem
from objetos import Porta
import os
from abc import abstractmethod

class Game:
    def __init__(self):
        #Criando a Tela do Jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA,constantes.ALTURA))
        self.imagem_jogador = None
        pygame.display.set_caption(constantes.TITULO)
        self.clock = pygame.time.Clock()
        self.esta_rodando = True
        self.jogando = False
        self.direcao = 0
        self.teclas_pressionadas = {'a': False, 's': False, 'd': False, 'w': False}
        self.velocidade = 0


    def novo_jogo(self):
        #instancia as classes
        self.rodar()


    def rodar(self):
        #loop do jogo
        self.jogando = True
        sala = Sala()
        jogador = Personagem(self.imagem_jogador, self.velocidade)
        porta_saida = Porta(self.tela, 0.75*constantes.LARGURA, constantes.Y_PAREDE_SUPERIOR)
        grupo_objetos_interativos = pygame.sprite.Group()
        grupo_sala = pygame.sprite.GroupSingle()
        grupo_objetos_interativos.add(porta_saida)
        grupo_sala.add(sala)
        while self.jogando:
            self.clock.tick(constantes.FPS)
            self.eventos()
            grupo_sala.draw(self.tela)
            grupo_objetos_interativos.draw(self.tela)
            jogador.mover_jogador(self.direcao)
            jogador.desenhar_jogador(self.tela)
            jogador.checar_interacao(grupo_objetos_interativos)
            pygame.display.update()


    def eventos(self):
        #Define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.jogando = False
                self.esta_rodando = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: #K_a=Tecla a
                    self.direcao = "a"
                    self.teclas_pressionadas['a'] = True
                elif event.key == pygame.K_w:
                    self.direcao = "w"
                    self.teclas_pressionadas['w'] = True
                elif event.key == pygame.K_d:
                    self.direcao = "d"
                    self.teclas_pressionadas['d'] = True
                elif event.key == pygame.K_s:
                    self.direcao = "s"
                    self.teclas_pressionadas['s'] = True
                elif event.key == pygame.K_ESCAPE:
                    self.jogando = False
                    self.esta_rodando = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.direcao = 0
                    self.teclas_pressionadas['a'] = False
                elif event.key == pygame.K_w:
                    self.direcao = 0
                    self.teclas_pressionadas['w'] = False
                elif event.key == pygame.K_d:
                    self.direcao = 0
                    self.teclas_pressionadas['d'] = False
                elif event.key == pygame.K_s:
                    self.direcao = 0
                    self.teclas_pressionadas['s'] = False
                for tecla in ('a','w','s','d'):
                    if self.teclas_pressionadas[tecla]:
                        self.direcao = tecla     


    def mostrar_tela_inicio(self):
        caminho_tela_inicio = os.path.join(constantes.DIRETORIO_IAMGENS, constantes.TELA_INICIO)
        tela_inicio = pygame.image.load(caminho_tela_inicio).convert()
        tela_inicio = pygame.transform.scale(tela_inicio, (1000, 800))
        retangulo_tela_inicio = tela_inicio.get_rect()
        retangulo_tela_inicio.midtop = (constantes.LARGURA/2,0)
        self.tela.blit(tela_inicio, retangulo_tela_inicio)

        menu = Menu(self.tela, tela_inicio)
        pygame.display.flip()
        menu.rodar_menu()
        self.esta_rodando = menu.esta_rodando
        self.imagem_jogador = menu.imagem_jogador
        self.velocidade = menu.velocidade
	
                    
    def game_over(self):
        #TODO
        pass 


class Sala(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        caminho_sala = os.path.join(constantes.DIRETORIO_IAMGENS, constantes.IMAGEM_SALA)
        self.image = pygame.image.load(caminho_sala).convert()
        self.image = pygame.transform.scale(self.image, (constantes.LARGURA, constantes.ALTURA))
        self.rect = self.image.get_rect()


g = Game()
g.mostrar_tela_inicio()

while g.esta_rodando:
    g.novo_jogo()
    g.game_over()