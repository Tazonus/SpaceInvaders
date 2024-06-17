from typing import Any, List
import pygame
from pygame.sprite import Group

class Alien(pygame.sprite.Sprite):
    def __init__(self, scale, x, y, type = 'f'):
        super().__init__()
        self.scale = scale
        self.type = type
        file_path = 'graphics/' + type + '.png'
        self.image = pygame.transform.scale(pygame.image.load(file_path).convert_alpha(),(scale *2/3, scale/3))
        self.rect = self.image.get_rect(topleft =(x,y))

    def update(self, direction, speed) -> None:
        self.flip_image()
        self.rect.x += direction * speed
        return super().update(direction, speed)
    

    def flip_image(self):
            if self.type.endswith('_flip'):
                self.type = self.type[0]
            else:
                 self.type += '_flip'

            file_path = 'graphics/' + self.type + '.png'
            pygame.transform.scale(pygame.image.load(file_path).convert_alpha(),(self.scale *2/3, self.scale/3))
