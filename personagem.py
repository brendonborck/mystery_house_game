import pygame
import os
import constantes

class Personagem(pygame.sprite.Sprite):
    def __init__(self, imagem_jogador, velocidade):
        super().__init__()
        self.caminho_imagem = os.path.join(constantes.DIRETORIO_IAMGENS, imagem_jogador)
        self.largura = 60
        self.altura = 80
        self.direcao = 0
        self.venceu_sala = False
        self.image = pygame.image.load(self.caminho_imagem).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.largura, self.altura))
        self.rect = self.image.get_rect()
        self.mask_on = self.definir_mask_on()
        self.mask_off = self.definir_mask_off()
        self.mask = self.mask_off
        self.x = (constantes.LARGURA - self.largura)/2
        self.y = (constantes.ALTURA + constantes.Y_PAREDE_SUPERIOR - 6)/2 - self.altura
        self.velocidade = velocidade
        self.objetos_interagidos = []


    def desenhar_jogador(self, tela):
        self.rect.topleft = (self.x, self.y)
        tela.blit(self.image, self.rect) 


    def mover_jogador(self):
        x_min = 0
        x_max = constantes.LARGURA
        y_min = constantes.Y_PAREDE_SUPERIOR
        y_max = constantes.ALTURA
        delta_y_3d = 0.7 * self.altura
        
        if self.direcao == "w" and self.y > y_min - delta_y_3d:
            self.y = self.y - self.velocidade
        if self.direcao == "s" and self.y < y_max - self.altura:
            self.y = self.y + self.velocidade
        if self.direcao == "a" and self.x > x_min:
            self.x = self.x - self.velocidade
        if self.direcao == "d" and self.x < x_max - self.largura:
            self.x = self.x + self.velocidade


    def agir(self):
        self.mask = self.mask_on


    def parar_agir(self):
        self.mask = self.mask_off


    def definir_mask_on(self):
        mask = pygame.mask.from_surface(self.image)
        mask.clear()
        largura_mask = 0.5*self.largura
        altura_mask = 0.3*self.altura + 1
        posicao = ((self.largura - largura_mask)/2, self.altura - altura_mask)
        retangulo = pygame.mask.Mask((largura_mask, altura_mask), True)
        mask.draw(retangulo, posicao)
        return mask


    def definir_mask_off(self):
        return pygame.mask.Mask((0, 0), False)


    def checar_interacao(self, grupo_sprites):
        interacoes = pygame.sprite.spritecollide(self, grupo_sprites, False, pygame.sprite.collide_mask)
        if interacoes:
            for objeto in interacoes:
                if objeto not in self.objetos_interagidos:
                    self.objetos_interagidos.append(objeto)
                objeto.interacao(self)
        else:
            for objeto in self.objetos_interagidos:
                objeto.pos_interacao()
                self.objetos_interagidos.remove(objeto)