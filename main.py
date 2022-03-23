
from cgitb import text
import pygame
import constantes
import sprites
import os
class Game:
    def __init__(self):
        #Criando a Tela do Jogo
        pygame.init()
        pygame.mixer.init()
        self.tela=pygame.display.set_mode((constantes.LARGURA,constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO)
        self.clock=pygame.time.Clock()
        self.esta_rodando=True
        self.fonte=pygame.font.match_font(constantes.FONTE)
        self.carregar_arquivos()

    def novo_jogo(self):
        #instancia as classes
        self.sprites=pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        #loop do jogo
        self.jogando=True
        while self.jogando:
            self.clock.tick(constantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()
    
    def eventos(self):
        #Define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando=False
                self.esta_rodando=False
    
    def atualizar_sprites(self):
        self.sprites.update()

    def desenhar_sprites(self):
        self.tela.fill(constantes.PRETO) #Limpando a Tela
        self.sprites.draw(self.tela)
        pygame.display.flip()

    def carregar_arquivos(self):
        #Carregar arquivos
        diretorio=os.path.join(os.getcwd(),'imagens')
        self.diretorio_audios=os.path.join(os.getcwd(),'audio')
        self.spritesheet=os.path.join(diretorio,constantes.SPRITESHEET)
        self.tela_inicio=os.path.join(diretorio,constantes.TELA_INICIO)
        self.tela_inicio=pygame.image.load(self.tela_inicio).convert()

    def mostrar_texto(self,texto,tamanho_fonte,cor,x,y):
        #Exibe um texto na tela do jogo
        fonte=pygame.font.Font(self.fonte,tamanho_fonte)
        texto=fonte.render(texto,True,cor)
        text_rect=texto.get_rect()
        text_rect.midtop=(x,y)
        self.tela.blit(texto,text_rect)

    def mostrar_start_logo(self,x,y):
        star_logo_rect=self.tela_inicio.get_rect()
        star_logo_rect.midtop=(x,y)
        self.tela.blit(self.tela_inicio,star_logo_rect)

    def mostrar_tela_start(self):
        self.mostrar_start_logo(constantes.LARGURA/2,20 )
        self.mostrar_texto('Se está preparado, pressione uma tecla',32,constantes.AZUL,constantes.LARGURA/2,constantes.ALTURA/2)
        pygame.display.flip()
        esperando=True
        while esperando:
            self.clock.tick(constantes.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando=False
                    self.esta_rodando=False 
                if event.type == pygame.KEYUP:
                    esperando=False
    def game_over(self):
        pass 

g=Game()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.game_over()