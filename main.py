from cgitb import text
import pygame
import constantes
import os
import time

class Game:
    def __init__(self):
        #Criando a Tela do Jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA,constantes.ALTURA))
        self.tela_inicio = None
        self.imagem_jogador = None
        pygame.display.set_caption(constantes.TITULO)
        self.clock = pygame.time.Clock()
        self.esta_rodando = True
        self.jogando = False
        self.fonte = pygame.font.match_font(constantes.FONTE)
        self.carregar_arquivos()
        self.direcao = 0
        self.teclas_pressionadas = {'a': False, 's': False, 'd': False, 'w': False}
        self.velocidade = 0


    def novo_jogo(self):
        #instancia as classes
        self.rodar()


    def rodar(self):
        #loop do jogo
        self.jogando = True
        background = Sala()
        jogador = Personagem(self.imagem_jogador, self.velocidade)
        jogador.desenhar_jogador(self.tela)
        while self.jogando:
            self.clock.tick(constantes.FPS)
            self.eventos()
            background.desenhar_sala(self.tela)
            jogador.mover_jogador(self.direcao)
            jogador.desenhar_jogador(self.tela)
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


    def carregar_arquivos(self):
        #Carregar arquivos
        diretorio_arquivos = os.path.join(os.getcwd(),'assets')
        diretorio_imagens = os.path.join(diretorio_arquivos,"imagens")
        self.tela_inicio = os.path.join(diretorio_imagens,constantes.TELA_INICIO)
        self.tela_inicio = pygame.image.load(self.tela_inicio).convert()
        self.tela_inicio = pygame.transform.scale(self.tela_inicio, (1000, 800))


    def mostrar_texto(self,mensagem,tamanho_fonte,cor,x,y):
        #Exibe um texto na tela do jogo
        fonte = pygame.font.Font(self.fonte,tamanho_fonte)
        texto = fonte.render(mensagem,True,cor)
        retangulo_texto = texto.get_rect()
        retangulo_texto.midtop = (x,y)
        self.tela.blit(texto,retangulo_texto)


    def mostrar_tela_inicio(self):
        retangulo_tela = self.tela_inicio.get_rect()
        retangulo_tela.midtop = (constantes.LARGURA/2,0)
        self.tela.blit(self.tela_inicio, retangulo_tela)

        menu = Menu(self.tela, self.tela_inicio, self.mostrar_texto, self.clock)
        pygame.display.flip()
        menu.rodar_menu()
        self.esta_rodando = menu.esta_rodando
        self.imagem_jogador = menu.imagem_jogador
        self.velocidade = menu.velocidade
	
                    
    def game_over(self):
        #TODO
        pass 


class Menu():
    def __init__(self, tela, tela_inicio, mostrar_texto_func, clock):
        self.tela = tela
        self.tela_inicio = tela_inicio
        self.mostrar_texto_func = mostrar_texto_func
        self.clock = clock
        self.esta_rodando = True
        self.jogando = False
        self.tamanho_fonte = 35
        self.fonte = pygame.font.match_font(constantes.FONTE)
        self.imagem_jogador = None
        self.velocidade = None


    def mostrar_opcoes(self, cores):
        self.mostrar_texto_func('Modo 1', self.tamanho_fonte, cores[0], constantes.LARGURA/2, constantes.ALTURA * 0.7)
        self.mostrar_texto_func('Modo 2', self.tamanho_fonte, cores[1], constantes.LARGURA/2, constantes.ALTURA * 0.8)
        self.mostrar_texto_func('Modo 3', self.tamanho_fonte, cores[2], constantes.LARGURA/2, constantes.ALTURA * 0.9)
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
        match botao_selecionado:
            case 0:
                self.imagem_jogador = "player1.png"
                self.velocidade = 10
            case 1:
                self.imagem_jogador = "player2.png"
                self.velocidade = 10
            case 2:
                self.imagem_jogador = "player1.png"
                self.velocidade = 20


class Sala(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.diretorio_arquivos = os.path.join(os.getcwd(),'assets')
        self.diretorio_imagens = os.path.join(self.diretorio_arquivos,"imagens")
        self.sala = os.path.join(self.diretorio_imagens,constantes.IMAGEM_SALA)
        self.sala = pygame.image.load(self.sala).convert()
        self.sala = pygame.transform.scale(self.sala, (constantes.LARGURA, constantes.ALTURA))


    def desenhar_sala(self,tela):
       tela.blit(self.sala,(0,0)) 


class Personagem(pygame.sprite.Sprite):
    def __init__(self, imagem_jogador, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.diretorio_arquivos = os.path.join(os.getcwd(), 'assets')
        self.diretorio_imagens = os.path.join(self.diretorio_arquivos, "imagens")
        self.player = os.path.join(self.diretorio_imagens, imagem_jogador)
        self.player = pygame.image.load(self.player).convert_alpha()
        self.x = constantes.LARGURA/2
        self.y = constantes.ALTURA/2
        self.altura = 80
        self.largura = 60
        self.velocidade = velocidade


    def desenhar_jogador(self,tela):
        self.player = pygame.transform.scale(self.player,(self.largura, self.altura))
        tela.blit(self.player,(self.x,self.y)) 


    def mover_jogador(self,direcao):
        x_min = 0
        x_max = constantes.LARGURA
        y_min = 150
        y_max = constantes.ALTURA
        
        if direcao == "w" and self.y > y_min:
            self.y = self.y - self.velocidade
        if direcao == "s" and self.y < y_max - self.altura:
            self.y = self.y + self.velocidade
        if direcao == "a" and self.x > x_min:
            self.x = self.x - self.velocidade
        if direcao == "d" and self.x < x_max - self.largura:
            self.x = self.x + self.velocidade
            

g=Game()
g.mostrar_tela_inicio()

while g.esta_rodando:
    g.novo_jogo()
    g.game_over()