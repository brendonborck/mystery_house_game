import pygame
import os
import constants

class Player(pygame.sprite.Sprite):
    """
        Classe que define como será o personagem principal
    """
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
        self.x = int(0.012*constants.WIDTH)*10
        self.y = int(0.088*constants.HEIGHT)*10
        self.speed = speed
        self.interacted_objects = []
        self.pocket_objects = []


    def draw_player(self):
        self.rect.center = (self.x, self.y)
        constants.SCREEN.blit(self.image, self.rect) 


    def move_player(self, obj_rects):
        if self.direction == "w" and self.limitations_w(obj_rects):
            self.y = self.y - self.speed
        elif self.direction == "s" and self.limitations_s(obj_rects):
            self.y = self.y + self.speed
        elif self.direction == "a" and self.limitations_a(obj_rects):
            self.x = self.x - self.speed
        elif self.direction == "d" and self.limitations_d(obj_rects):
            self.x = self.x + self.speed


    def limitations_w(self, obj_rects):
        y_min = constants.Y_SUPERIOR_WALL
        delta_y_3d = 0.2 * self.height

        limitations = [
            self.y > y_min - delta_y_3d
        ]
        for obj_rect in obj_rects:
            y_min = obj_rect.center[1] - obj_rect.h/2
            y_max = obj_rect.center[1] + obj_rect.h/2
            x_max = obj_rect.center[0] + obj_rect.w/2
            x_min = obj_rect.center[0] - obj_rect.w/2
            if(self.x >= x_min - self.width/2 and self.x <= x_max + self.width/2):
                limitations.append(not (self.y <= y_max - delta_y_3d + self.speed and self.y >= y_min - self.height/2 + self.speed))
        return all(limitations)


    def limitations_s(self, obj_rects):
        y_max = constants.HEIGHT
        delta_y_3d = 0.2 * self.height

        limitations = [
            self.y < y_max - self.height/2
        ]
        for obj_rect in obj_rects:
            y_min = obj_rect.center[1] - obj_rect.h/2
            y_max = obj_rect.center[1] + obj_rect.h/2
            x_max = obj_rect.center[0] + obj_rect.w/2
            x_min = obj_rect.center[0] - obj_rect.w/2
            if(self.x >= x_min - self.width/2 and self.x <= x_max + self.width/2):
                limitations.append(not (self.y <= y_max - delta_y_3d - self.speed and self.y >= y_min - self.height/2 - self.speed))
        return all(limitations)


    def limitations_a(self, obj_rects):
        x_min = 0
        delta_y_3d = 0.2 * self.height

        limitations = [
            self.x > x_min + self.width/2
        ]
        for obj_rect in obj_rects:
            y_min = obj_rect.center[1] - obj_rect.h/2
            y_max = obj_rect.center[1] + obj_rect.h/2
            x_max = obj_rect.center[0] + obj_rect.w/2
            x_min = obj_rect.center[0] - obj_rect.w/2
            if(self.y >= y_min - self.height/2 and self.y <= y_max - delta_y_3d):
                limitations.append(not (self.x <= x_max + self.width/2 + self.speed and self.x >= x_min - self.width/2 + self.speed))
        return all(limitations)


    def limitations_d(self, obj_rects):
        x_max = constants.WIDTH
        delta_y_3d = 0.2 * self.height

        limitations = [
            self.x < x_max - self.width/2
        ]
        for obj_rect in obj_rects:
            y_min = obj_rect.center[1] - obj_rect.h/2
            y_max = obj_rect.center[1] + obj_rect.h/2
            x_max = obj_rect.center[0] + obj_rect.w/2
            x_min = obj_rect.center[0] - obj_rect.w/2
            if(self.y >= y_min - self.height/2 and self.y <= y_max - delta_y_3d):
                limitations.append(not (self.x <= x_max + self.width/2 - self.speed and self.x >= x_min - self.width/2 - self.speed))
        return all(limitations)


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