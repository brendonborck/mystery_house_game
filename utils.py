import pygame
import constantes

class Utils:

    def __init__(self):
        pass

    @staticmethod
    def mostrar_texto(tela, mensagem, tamanho_fonte, cor, x, y):
        #Exibe um texto na tela do jogo
        nome_fonte = pygame.font.match_font(constantes.FONTE)
        fonte = pygame.font.Font(nome_fonte, tamanho_fonte)
        texto = fonte.render(mensagem, True, cor)
        retangulo_texto = texto.get_rect()
        retangulo_texto.center = (x, y)
        tela.blit(texto, retangulo_texto)
        


class Texto(pygame.sprite.Sprite):

    def __init__(self, mensagem, tamanho_fonte, x_fundo, y_fundo, x_texto, y_texto, largura, altura, cor_texto, cor_fundo = constantes.PRETO):
        super().__init__()
        nome_fonte = pygame.font.match_font(constantes.FONTE)
        fonte = pygame.font.Font(nome_fonte, tamanho_fonte)
        texto = fonte.render(mensagem, True, cor_texto)
        
        self.image = pygame.Surface([largura, altura])
        self.image.fill(cor_fundo)
        self.rect = self.image.get_rect()
        self.rect.center = (x_fundo ,y_fundo)

        retangulo_texto = texto.get_rect()
        x = x_texto - retangulo_texto.w/2
        y = y_texto - retangulo_texto.h/2
        self.image.blit(texto, (x, y))
