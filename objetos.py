import pygame
import constantes
from utils import Texto, Utils
import os
import time
from abc import abstractmethod

class ObjetosInterativos(pygame.sprite.Sprite):
    
    def __init__(self, tela, clock, caminho_imagem, x, y, modo_posicao, escala = None):
        super().__init__()
        self.tela = tela
        self.clock = clock
        self.image = pygame.image.load(caminho_imagem).convert_alpha()
        if escala:
            self.image = pygame.transform.scale(self.image, escala)
        self.rect = self.image.get_rect()
        if modo_posicao=='center':
            self.rect.center = (x, y)
        elif modo_posicao=='bottomleft':
            self.rect.bottomleft = (x, y)
        self.largura = self.rect.width
        self.altura = self.rect.height
        self.mask = self.definir_mask()
        

    @abstractmethod
    def interacao(self):
        pass
    
    
    @abstractmethod
    def pos_interacao(self):
        pass

    
    @abstractmethod
    def definir_mask(self):
        pass


class Porta(ObjetosInterativos):
    
    def __init__(self, tela, clock, x, y, modo_posicao):
        self.imagem_porta_fechada = os.path.join(constantes.DIRETORIO_IAMGENS, 'porta_fechada.png')
        self.imagem_porta_aberta = os.path.join(constantes.DIRETORIO_IAMGENS, 'porta_aberta.png')
        super().__init__(tela, clock, self.imagem_porta_fechada, x, y, modo_posicao)
        self.enigma_completo = False

    
    def interacao(self, jogador):        
        self.print_pop_up()

        vendo_pop_up = True
        senha_digitada = ''
        senha = 'senha'
        while vendo_pop_up:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #TODO
                    pass
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        vendo_pop_up = False
                        jogador.parar_agir()
                    elif event.key == pygame.K_RETURN:
                        vendo_pop_up = False
                        jogador.parar_agir()
                        if senha_digitada == senha:
                            self.enigma_completo = True
                        else:
                            self.enigma_completo = False
                    elif event.key == pygame.K_BACKSPACE:
                        senha_digitada = senha_digitada[:-1]
                        self.print_senha(senha_digitada)
                    elif event.key == pygame.K_SPACE:
                        senha_digitada += event.unicode
                        self.print_senha(senha_digitada)
                    elif event.unicode:
                        senha_digitada += event.unicode
                        self.print_senha(senha_digitada)

        if self.enigma_completo:
            self.image = pygame.image.load(self.imagem_porta_aberta).convert_alpha()
            self.tela.blit(self.image, self.rect)
            jogador.desenhar_jogador(self.tela)
            self.print_mensagem('Senha correta!', 1.4)
            jogador.venceu_sala = True
        else:
            self.print_mensagem('Senha incorreta', 0.8)


    def pos_interacao(self):
        pass


    def definir_mask(self):
        mask = pygame.mask.from_surface(self.image)
        mask.clear()
        largura_mask = 0.2*self.largura
        altura_mask = self.altura
        posicao = ((self.largura - largura_mask)/2, self.altura - altura_mask)
        retangulo = pygame.mask.Mask((largura_mask, altura_mask), True)
        mask.draw(retangulo, posicao)
        return mask


    def print_pop_up(self):
        x_fundo = constantes.LARGURA/2
        y_fundo1 = constantes.ALTURA/2
        y_fundo2 = 0.51*constantes.ALTURA
        mensagem1 = 'Trancada'
        mensagem2 = 'Insira a senha:'
        tamanho_fonte1 = 40
        tamanho_fonte2 = 20
        cor = constantes.BRANCO
        largura = 0.5*constantes.LARGURA
        altura1 = 0.23*constantes.ALTURA
        altura2 = 0.03*constantes.ALTURA
        x_texto = largura/2
        y_texto1 = 0.26*altura1
        y_texto2 = 0.5*altura2
        grupo_texto = pygame.sprite.Group()
        texto1 = Texto(mensagem1, tamanho_fonte1, x_fundo, y_fundo1, x_texto, y_texto1, largura, altura1, cor)
        texto2 = Texto(mensagem2, tamanho_fonte2, x_fundo, y_fundo2, x_texto, y_texto2, largura, altura2, cor)
        grupo_texto.add(texto1, texto2)

        grupo_texto.draw(self.tela)
        pygame.display.update()
        self.print_senha('')


    def print_senha(self, senha_digitada):
        x_fundo = constantes.LARGURA/2
        y_fundo = 0.57*constantes.ALTURA
        mensagem = senha_digitada
        tamanho_fonte = 16
        cor = constantes.PRETO
        largura = 0.4*constantes.LARGURA
        altura = 0.03*constantes.ALTURA
        x_texto = 0.5*largura
        y_texto = 0.5*altura
        grupo_texto = pygame.sprite.Group()
        texto = Texto(mensagem, tamanho_fonte, x_fundo, y_fundo, x_texto, y_texto, largura, altura, cor, constantes.BRANCO)
        grupo_texto.add(texto)

        grupo_texto.draw(self.tela)
        pygame.display.update()


    def print_mensagem(self, mensagem, tempo):
        x_fundo = constantes.LARGURA/2
        y_fundo = constantes.ALTURA/2
        tamanho_fonte = 40
        cor = constantes.BRANCO
        largura = 0.5*constantes.LARGURA
        altura = 0.2*constantes.ALTURA
        x_texto = 0.5*largura
        y_texto = 0.5*altura
        grupo_texto = pygame.sprite.Group()
        texto = Texto(mensagem, tamanho_fonte, x_fundo, y_fundo, x_texto, y_texto, largura, altura, cor)
        grupo_texto.add(texto)

        grupo_texto.draw(self.tela)
        pygame.display.update()
        time.sleep(tempo)
        for event in pygame.event.get():
            pass


class Quadro(ObjetosInterativos):
    
    def __init__(self, tela, clock, x, y, modo_posicao):
        self.imagem_quadro = os.path.join(constantes.DIRETORIO_IAMGENS, 'quadro.png')
        super().__init__(tela, clock, self.imagem_quadro, x, y, modo_posicao, (69, 74))

    
    def interacao(self, jogador):
        x_fundo, y_fundo = (constantes.LARGURA/2, constantes.ALTURA/2)
        mensagem = 'Senha: 01110011 01100101 01101110 01101000 01100001'
        tamanho_fonte = 20
        cor = constantes.BRANCO
        largura = 0.72*constantes.LARGURA
        altura = 0.1*constantes.ALTURA
        x_texto = largura/2
        y_texto = altura/2
        texto = Texto(mensagem, tamanho_fonte, x_fundo, y_fundo, x_texto, y_texto, largura, altura, cor)
        grupo_texto = pygame.sprite.Group()
        grupo_texto.add(texto)
        grupo_texto.draw(self.tela)
        pygame.display.update()
        
        vendo_pop_up = True
        while vendo_pop_up:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #TODO
                    pass
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        vendo_pop_up = False
                    elif event.key == pygame.K_ESCAPE:
                        vendo_pop_up = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_e:
                        jogador.parar_agir()


    def pos_interacao(self):
        pass


    def definir_mask(self):
        largura_mask = self.largura
        altura_mask = constantes.Y_PAREDE_SUPERIOR - self.rect.top
        mask = pygame.mask.Mask((largura_mask, altura_mask), False)
        largura_retangulo = 0.1*self.largura
        altura_retangulo = altura_mask
        posicao = ((largura_mask - largura_retangulo)/2, 0)
        retangulo = pygame.mask.Mask((largura_retangulo, altura_retangulo), True)
        mask.draw(retangulo, posicao)
        return mask
        
        
class Pergaminho(ObjetosInterativos):
    
    def __init__(self, tela, clock, x, y, modo_posicao):
        self.imagem_pergaminho = os.path.join(constantes.DIRETORIO_IAMGENS, 'pergaminho.png')
        super().__init__(tela, clock, self.imagem_pergaminho, x, y, modo_posicao, (45, 55))

    
    def interacao(self, jogador):
        x_fundo, y_fundo = (constantes.LARGURA/2, constantes.ALTURA/2)
        largura = 0.87*constantes.LARGURA
        altura = 0.24*constantes.ALTURA
        imagem = pygame.Surface([largura, altura])
        imagem.fill(constantes.PRETO)
        retangulo = imagem.get_rect()
        retangulo.center = (x_fundo ,y_fundo)
        self.tela.blit(imagem, retangulo)
        
        tamanho_fonte = 16
        cor = constantes.BRANCO
        x_texto = x_fundo
        y_texto1 = 0.44*constantes.ALTURA
        y_texto2 = 0.48*constantes.ALTURA
        y_texto3 = 0.52*constantes.ALTURA
        y_texto4 = 0.56*constantes.ALTURA
        mensagem1 = "Bem vindo a Mistery House!"
        mensagem2 = "Você não se lembra como veio parar aqui, mas não se preocupe, tudo será explicado no tempo"
        mensagem3 = "certo. A única coisa que posso te dizer nesse momento é que, por muitas vezes, a vida"
        mensagem4 = "parece ser apenas preto no branco, mas, na verdade, ela não é. Tudo não é sempre 0 ou 1."
        Utils().mostrar_texto(self.tela, mensagem1, int(1.25*tamanho_fonte), cor, x_texto, y_texto1)
        Utils().mostrar_texto(self.tela, mensagem2, tamanho_fonte, cor, x_texto, y_texto2)
        Utils().mostrar_texto(self.tela, mensagem3, tamanho_fonte, cor, x_texto, y_texto3)
        Utils().mostrar_texto(self.tela, mensagem4, tamanho_fonte, cor, x_texto, y_texto4)


        pygame.display.update()
        
        vendo_pop_up = True
        while vendo_pop_up:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #TODO
                    pass
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        vendo_pop_up = False
                    elif event.key == pygame.K_ESCAPE:
                        vendo_pop_up = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_e:
                        jogador.parar_agir()


    def pos_interacao(self):
        pass


    def definir_mask(self):
        largura_mask = self.largura
        altura_mask = self.altura
        mask = pygame.mask.Mask((largura_mask, altura_mask), False)
        largura_retangulo = 0.8*largura_mask
        altura_retangulo = 0.8*altura_mask
        posicao = ((largura_mask - largura_retangulo)/2, (altura_mask - largura_retangulo)/2)
        retangulo = pygame.mask.Mask((largura_retangulo, altura_retangulo), True)
        mask.draw(retangulo, posicao)
        return mask        

