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