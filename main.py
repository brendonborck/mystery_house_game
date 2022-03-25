
from cgitb import text
import pygame
import constantes
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
        self.direcao=0
        self.teclas_pressionadas = {'a': False, 's': False, 'd': False, 'w': False}

    def novo_jogo(self):
        #instancia as classes
        self.rodar()

    def rodar(self):
        #loop do jogo
        self.jogando=True
        Backgorund=Sala()
        Jogador=Personagem()
        Jogador.desenhar_jogador(self.tela)
        while self.jogando:
            self.clock.tick(constantes.FPS)
            self.eventos()
            self.tela.fill((150,255,255))
            Backgorund.Desenhar_Sala(self.tela)
            Jogador.mover_jogador(self.direcao)
            Jogador.desenhar_jogador(self.tela)
            pygame.display.update()
    
    def eventos(self):
        #Define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando=False
                self.esta_rodando=False
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
    def carregar_arquivos(self):
        #Carregar arquivos
        diretorio=os.path.join(os.getcwd(),'assets')
        diretorio=os.path.join(diretorio,"imagens")
        #self.diretorio_audios=os.path.join(os.getcwd(),'assets')
        self.spritesheet=os.path.join(diretorio,constantes.SPRITESHEET)
        self.tela_inicio=os.path.join(diretorio,constantes.TELA_INICIO)
        self.tela_inicio=pygame.image.load(self.tela_inicio).convert()
        self.tela_inicio=pygame.transform.scale(self.tela_inicio, (1000, 800))

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
        self.mostrar_start_logo(constantes.LARGURA/2,0)
        self.mostrar_texto('Se está preparado, pressione uma tecla',50,constantes.BRANCO,constantes.LARGURA/2,constantes.ALTURA * 0.5)
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


class Sala(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.diretorio=os.path.join(os.getcwd(),'assets')
        self.diretorio=os.path.join(self.diretorio,"imagens")
        self.sala=os.path.join(self.diretorio,constantes.SALA)
        self.sala=pygame.image.load(self.sala).convert()
        self.sala = pygame.transform.scale(self.sala, (constantes.LARGURA, constantes.ALTURA))

    def Desenhar_Sala(self,tela):
       tela.blit(self.sala,(0,0)) 

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.diretorio=os.path.join(os.getcwd(),'assets')
        self.diretorio=os.path.join(self.diretorio,"imagens")
        self.player=os.path.join(self.diretorio,constantes.JOGADOR)
        self.player=pygame.image.load(self.player).convert()
        self.x = constantes.LARGURA/2
        self.y = constantes.ALTURA/2
        self.altura = 80
        self.largura = 60

    def desenhar_jogador(self,tela):
        self.player=pygame.transform.scale(self.player,(self.largura, self.altura))
        tela.blit(self.player,(self.x,self.y)) 

    def mover_jogador(self,direcao):
        x_min = 0
        x_max = 800
        y_min = 150
        y_max = constantes.ALTURA
        velocidade = 10
        
        if direcao == "w" and self.y > y_min:
            self.y = self.y - velocidade
        if direcao == "s" and self.y < y_max - self.altura:
            self.y = self.y + velocidade
        if direcao == "a" and self.x > x_min:
            self.x = self.x - velocidade
        if direcao == "d" and self.x < x_max - self.largura:
            self.x = self.x + velocidade
            

g=Game()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.game_over()
