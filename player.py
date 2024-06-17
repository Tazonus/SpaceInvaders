import pygame
from bullet import Bullet
class Player(pygame.sprite.Sprite):
    def __init__(self, screen_size, scale, speed = 5):
        super().__init__()
        self.screen_size = screen_size
        self.scale = scale
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load('player.png').convert_alpha(),(scale, scale/2))
        self.rect = self.image.get_rect(midbottom = (screen_size/2, screen_size * 99 / 100))
        
    def move(self, side):
        self.rect.x += self.speed * side

        #Out of bounds safeguard
        if self.rect.x < 0:
            self.rect.x = 0
        elif (self.screen_size - self.scale) < self.rect.x :
            self.rect.x = self.screen_size - self.scale

    def get_position(self):
        return (self.rect.x, self.rect.y)