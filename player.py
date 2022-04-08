import pygame
import os
import constants

class Player(pygame.sprite.Sprite):
    def __init__(self, player_image, speed):
        super().__init__()
        self.image_path = os.path.join(constants.IMAGES_DIR, player_image)
        self.width = 60
        self.height = 80
        self.direction = 0
        self.passed_room = False
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.mask_on = self.define_mask_on()
        self.mask_off = self.define_mask_off()
        self.mask = self.mask_off
        self.x = (constants.WIDTH - self.width)/2
        self.y = (constants.HEIGHT + constants.Y_SUPERIOR_WALL - 6)/2 - self.height
        self.speed = speed
        self.interacted_objects = []


    def draw_player(self, screen):
        self.rect.topleft = (self.x, self.y)
        screen.blit(self.image, self.rect) 


    def move_player(self):
        x_min = 0
        x_max = constants.WIDTH
        y_min = constants.Y_SUPERIOR_WALL
        y_max = constants.HEIGHT
        delta_y_3d = 0.7 * self.height
        
        if self.direction == "w" and self.y > y_min - delta_y_3d:
            self.y = self.y - self.speed
        if self.direction == "s" and self.y < y_max - self.height:
            self.y = self.y + self.speed
        if self.direction == "a" and self.x > x_min:
            self.x = self.x - self.speed
        if self.direction == "d" and self.x < x_max - self.width:
            self.x = self.x + self.speed


    def act(self):
        self.mask = self.mask_on


    def stop_acting(self):
        self.mask = self.mask_off


    def define_mask_on(self):
        mask = pygame.mask.from_surface(self.image)
        mask.clear()
        mask_width = 0.65*self.width
        mask_height = 0.3*self.height + 1
        position = ((self.width - mask_width)/2, self.height - mask_height)
        rect = pygame.mask.Mask((mask_width, mask_height), True)
        mask.draw(rect, position)
        return mask


    def define_mask_off(self):
        return pygame.mask.Mask((0, 0), False)


    def check_interaction(self, grupo_sprites):
        collisions = pygame.sprite.spritecollide(self, grupo_sprites, False, pygame.sprite.collide_mask)
        if collisions:
            for objeto in collisions:
                if objeto not in self.interacted_objects:
                    self.interacted_objects.append(objeto)
                objeto.interaction(self)
            return True
        else:
            for objeto in self.interacted_objects:
                objeto.after_interaction()
                self.interacted_objects.remove(objeto)
            return False