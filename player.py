import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_size, scale, speed = 5):
        super().__init__()
        self.screen_size = screen_size
        self.scale = scale
        self.speed = speed

        self.image = pygame.image.load('player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(scale, scale/2))
        self.rect = self.image.get_rect(midbottom = (screen_size/2,screen_size*99/100))
     
    def update(self):
        self.input_handling()
        
    def input_handling(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.move(1)
        elif keys[pygame.K_a]:
            self.move(-1)
    
    def move(self, side):
        self.rect.x += self.speed * side

        #Out of bounds safeguard
        if self.rect.x < 0:
            self.rect.x = 0
        elif (self.screen_size - self.scale) < self.rect.x :
            self.rect.x = self.screen_size - self.scale