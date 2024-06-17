import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, scale, speed = 5):
        super().__init__()
        self.scale = scale

        self.image = pygame.image.load('player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(scale, scale/2))
        self.rect = self.image.get_rect(midbottom = pos)

        self.speed = speed

    def input_handling(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
    def update(self):
        self.input_handling()