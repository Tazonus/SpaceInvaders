import pygame, sys
from player import Player
from alien import Alien
from config import scale

class Game:
    def __init__(self,screen_size):
        #General

        #Player
        self.player_sprite = Player(screen_size)
        self.player = pygame.sprite.GroupSingle(self.player_sprite)

        #zmiana planow

        #Aliens
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 5, cols = 11)
        self.alien_direction = 1

    def alien_setup(self, rows, cols):
        for row_index, row in enumerate(range(rows)):
            for col_index, column in enumerate(range(cols)):
                x = scale *7/8 + scale * col_index
                y = scale + scale * row_index
                
                type = 'f' 
                if row_index == 0:
                    type = 'b'
                elif 1 <= row_index <= 2:
                    type = 'm'
                elif 3 <= row_index <= 5:
                    type = 'f'
                alien_sprite = Alien(x, y, type)
                self.aliens.add(alien_sprite)
            
    def alien_colisioncheck(self):
        aliens = self.aliens.sprites()
        for alien in aliens:
            if alien.rect.x + scale * 3/5 >= screen_size:
                self.alien_direction = -1
                self.alien_forward()
            elif alien.rect.x < 0:
                self.alien_direction = 1
                self.alien_forward()
    
    def alien_forward(self):
        aliens = self.aliens.sprites()
        for alien in aliens:
            alien.rect.y += scale/40
            
    def run(self):
        '''GameLoop here:'''

        self.player.update()
        self.aliens.update(self.alien_direction, speed = 1)
        self.alien_colisioncheck()

        self.player.draw(screen)
        self.aliens.draw(screen)
        self.player.sprite.bulletGroup.draw(screen)


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


        