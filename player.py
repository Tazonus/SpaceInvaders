from typing import Any
import pygame
from bullet import Bullet
from config import scale

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_size, speed = 5):
        super().__init__()
        self.screen_size = screen_size
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load('graphics/player.png').convert_alpha(),(scale, scale/2))
        self.rect = self.image.get_rect(midbottom = (screen_size/2, screen_size * 99 / 100))

        self.charged = True
        self.bullet = Bullet(5, self.rect.center, True)
        self.bullet.rect.y = -20
        self.bulletGroup = pygame.sprite.Group(self.bullet)

    
    def move(self, side):
        self.rect.x += self.speed * side

        #Out of bounds safeguard
        if self.rect.x < 0:
            self.rect.x = 0
        elif (self.screen_size - scale) < self.rect.x :
            self.rect.x = self.screen_size - scale

    def get_position(self):
        return (self.rect.x, self.rect.y)
       
    def input_handling(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.move(1)
        elif keys[pygame.K_LEFT]:
            self.move(-1)
        if keys[pygame.K_z]:
            if self.charged:
                self.charged = False
                pos = self.rect.midtop
                self.bullet.set_position(pos)


                        
    def update(self) -> None:
        self.input_handling()
        self.bulletGroup.update()
        if self.bullet.rect.y <= 0:
            self.charged = True
        return super().update()