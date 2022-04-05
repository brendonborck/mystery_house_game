import pygame
import constantes
from menu import Menu
from personagem import Personagem
from objetos import Porta, Quadro
from utils import Texto
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
        quadro_x = 0.15*constantes.LARGURA
        quadro_y = 0.36*constantes.Y_PAREDE_SUPERIOR
        quadro = Quadro(self.tela, self.clock, quadro_x, quadro_y, 'center')
        porta_saida_x = 0.75*constantes.LARGURA
        porta_saida_y = constantes.Y_PAREDE_SUPERIOR
        porta_saida = Porta(self.tela, self.clock, porta_saida_x, porta_saida_y, 'bottomleft')
        grupo_objetos_interativos = pygame.sprite.Group()
        grupo_sala = pygame.sprite.GroupSingle()
        grupo_objetos_interativos.add(porta_saida, quadro)
        grupo_sala.add(sala)
        while self.jogando:
            self.clock.tick(constantes.FPS)
            self.eventos(jogador)
            grupo_sala.draw(self.tela)
            grupo_objetos_interativos.draw(self.tela)
            jogador.mover_jogador()
            jogador.desenhar_jogador(self.tela)
            interagiu = jogador.checar_interacao(grupo_objetos_interativos)
            if interagiu:
                for tecla in self.teclas_pressionadas:
                    self.teclas_pressionadas[tecla] = False
                jogador.direcao = 0
            pygame.display.update()
            if jogador.venceu_sala:
                self.jogando = False

    def eventos(self, jogador):
        #Define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.jogando = False
                self.esta_rodando = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s):
                    jogador.direcao = event.unicode
                    self.teclas_pressionadas[event.unicode] = True
                elif event.key == pygame.K_e:
                    jogador.agir()
                elif event.key == pygame.K_ESCAPE:
                    self.jogando = False
                    self.esta_rodando = False
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s):
                    jogador.direcao = 0
                    self.teclas_pressionadas[event.unicode] = False
                elif event.key == pygame.K_e:
                    jogador.parar_agir()
                for tecla in ('a','w','s','d'):
                    if self.teclas_pressionadas[tecla]:
                        jogador.direcao = tecla     


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
	
                    
    def fim_de_jogo(self):
        self.clock.tick(constantes.FPS)
        x_fundo = constantes.LARGURA/2
        y_fundo = constantes.ALTURA/2
        tamanho_fonte = 60
        mensagem = 'Você venceu!'
        cor = constantes.BRANCO
        largura = constantes.LARGURA
        altura = constantes.ALTURA
        x_texto = 0.5*largura
        y_texto = 0.5*altura
        grupo_texto = pygame.sprite.Group()
        texto = Texto(mensagem, tamanho_fonte, x_fundo, y_fundo, x_texto, y_texto, largura, altura, cor)
        grupo_texto.add(texto)

        grupo_texto.draw(self.tela)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.esta_rodando = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.esta_rodando = False


class Sala(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        caminho_sala = os.path.join(constantes.DIRETORIO_IAMGENS, constantes.IMAGEM_SALA)
        self.image = pygame.image.load(caminho_sala).convert()
        self.image = pygame.transform.scale(self.image, (constantes.LARGURA, constantes.ALTURA))
        self.rect = self.image.get_rect()


if __name__ == '__main__':
    g = Game()
    g.mostrar_tela_inicio()
    g.novo_jogo()

    while g.esta_rodando:
        g.fim_de_jogo()