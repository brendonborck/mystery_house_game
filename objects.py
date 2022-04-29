import pygame
from abc import abstractmethod

class InteractiveObjetcs(pygame.sprite.Sprite):
    """Classe que define os parametros de iteração para todos os móveis"""
    def __init__(self, image_path, x, y, position_mode, scale = None):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        if scale:
            self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        if position_mode == 'center':
            self.rect.center = (x, y)
        elif position_mode == 'bottomleft':
            self.rect.bottomleft = (x, y)
        self.width = self.rect.width
        self.height = self.rect.height
        self.mask = self.define_mask()
        

    @abstractmethod
    def interaction(self):
        pass
    
    
    @abstractmethod
    def after_interaction(self):
        pass

    
    @abstractmethod
    def define_mask(self):
        pass