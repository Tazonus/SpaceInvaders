from typing import Any
import pygame
from config import scale

class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, position, friendly = False):
        super().__init__()
        self.speed = speed
        self.friendly = friendly
        self.image = pygame.transform.scale(pygame.image.load('graphics/bullet.png').convert_alpha(),(scale/10, scale/2))
        self.image.fill('white')
        self.rect = self.image.get_rect(midbottom = position)

    def update(self) -> None:
        self.rect.y -= self.speed
        if self.rect.y<= 0:
            self.destroy()

    def set_position(self, position):
        self.rect.midbottom = position
    def get_position(self):
        return(self.rect.x, self.rect.y)
    
    def destroy(self):
        if self.friendly:
            self.rect.y = -scale
        else:
            self.kill()