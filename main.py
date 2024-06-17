import pygame, sys
from player import Player
from bullet import Bullet
from alien import Alien

class Game:
    def __init__(self,screen_size):
        #General
        self.scale = 64

        #Player
        self.player = Player(screen_size , self.scale)
        self.player_sprite = pygame.sprite.GroupSingle(self.player)

        self.projectile = Bullet(self.scale, -10)
        ### w space invaders nie można oddać kolejnego strzału dopóki obecny w nic nie trafi/dojdzie do końca mapy
        ### dlatego będę używał jednego obiektu zamiast tworzyć przy każdym wystrzale

        #Aliens
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 5, cols = 11)
        self.alien_direction = 1

    def run(self):
        '''GameLoop here:'''
        self.input_handling()
        self.projectile.update()
        self.aliens.update(self.alien_direction, speed = 1)
        self.alien_colisioncheck()

        self.player_sprite.draw(screen)
        self.aliens.draw(screen)


        screen.blit(self.projectile.image, self.projectile.get_position())

    def input_handling(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.player.move(1)
        elif keys[pygame.K_LEFT]:
            self.player.move(-1)
        if keys[pygame.K_z]:
            pos = self.player.get_position()
            self.projectile.shot(pos)
    
    def alien_setup(self, rows, cols):
        for row_index, row in enumerate(range(rows)):
            for col_index, column in enumerate(range(cols)):
                x = self.scale *7/8 + self.scale * col_index
                y = self.scale + self.scale * row_index
                
                type = 'f'
                if row_index == 0:
                    type = 'b'
                elif 1 <= row_index <= 2:
                    type = 'm'
                elif 3 <= row_index <= 5:
                    type = 'f'
                alien_sprite = Alien(self.scale, x, y, type)
                self.aliens.add(alien_sprite)
            
    def alien_colisioncheck(self):
        aliens = self.aliens.sprites()
        for alien in aliens:
            if alien.rect.x + self.scale * 3/5 >= screen_size:
                self.alien_direction = -1
                self.alien_forward()
            elif alien.rect.x < 0:
                self.alien_direction = 1
                self.alien_forward()
    def alien_forward(self):
        aliens = self.aliens.sprites()
        for alien in aliens:
            alien.rect.y += self.scale/40

if __name__ == '__main__':
    # Window managment:
    pygame.init()
    screen_size = 800
    screen = pygame.display.set_mode((screen_size, screen_size))
    # Window Details
    pygame.display.set_caption("Space Invader")
    icon = pygame.image.load('graphics/ufo.png') 
    pygame.display.set_icon(icon)

    # Logic and time
    game = Game(screen_size)
    clock = pygame.time.Clock()

    while True:
        screen.fill((0, 0, 0))
        #KeyCheck
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        game.run()
        pygame.display.flip()
        clock.tick(60)


        