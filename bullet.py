import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, scale, speed = -5):
        super().__init__()
        self.scale = scale
        self.speed = speed
        self.charged = True
        self.x = 0
        self.y = -scale
        self.image = pygame.transform.scale(pygame.image.load('graphics/bullet.png').convert_alpha(),(scale/4, scale/2))


    def shot(self,position):
        if self.charged == True:
            self.charged = False
            self.x ,self.y = position
            self.x += self.scale*8/19

    def update(self):
        self.y += self.speed
        if self.y<= 0:
            self.destroy()

    def destroy(self):
        self.charged = True
        self.y = -self.scale

    def get_position(self):
        return(self.x, self.y)