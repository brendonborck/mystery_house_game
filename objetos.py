import pygame
import constantes
from utils import Utils
import os
from abc import abstractmethod

class ObjetosInterativos(pygame.sprite.Sprite):
    
    def __init__(self, tela, caminho_imagem, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.tela = tela
        self.image = pygame.image.load(caminho_imagem).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        self.largura = self.rect.width
        self.altura = self.rect.height
        self.mask = self.definir_mask()
        

    @abstractmethod
    def acao(self):
        pass
    
    
    @abstractmethod
    def pos_acao(self):
        pass

    
    @abstractmethod
    def definir_mask(self):
        pass


class Porta(ObjetosInterativos):
    
    def __init__(self, tela, x, y):
        self.imagem_porta_fechada = os.path.join(constantes.DIRETORIO_IAMGENS, 'porta_fechada.png')
        self.imagem_porta_aberta = os.path.join(constantes.DIRETORIO_IAMGENS, 'porta_aberta.png')
        super().__init__(tela, self.imagem_porta_fechada, x, y)

    
    def acao(self):
        # abrir menu num loop
        largura_pop_up = 0.6*constantes.LARGURA
        altura_pop_up = 0.3*constantes.ALTURA
        cor = constantes.PRETO
        x, y = (constantes.LARGURA/2, constantes.ALTURA/2)
        pop_up = pygame.Surface([largura_pop_up, altura_pop_up])
        pop_up.fill(cor)
        retangulo_pop_up = pop_up.get_rect()
        retangulo_pop_up.center = (x, y)
        self.tela.blit(pop_up, retangulo_pop_up)
        self.image = pygame.image.load(self.imagem_porta_aberta).convert_alpha()
        mensagem = 'lero lero'
        tamanho_fonte = 80
        cor = constantes.BRANCO
        Utils().mostrar_texto(self.tela, mensagem, tamanho_fonte, cor, x, y)


    def pos_acao(self):
        self.image = pygame.image.load(self.imagem_porta_fechada).convert_alpha()


    def definir_mask(self):
        mask = pygame.mask.from_surface(self.image)
        mask.clear()
        largura_mask = 0.65*self.largura
        altura_mask = self.altura
        posicao = ((self.largura - largura_mask)/2, self.altura - altura_mask)
        retangulo = pygame.mask.Mask((largura_mask, altura_mask), True)
        mask.draw(retangulo, posicao)
        return mask