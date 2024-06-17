import pygame, sys
from player import Player
from bullet import Bullet

class Game:
    def __init__(self,screen_size):
        scale = 64
        self.player = Player(screen_size , scale)
        self.projectile = Bullet(scale, -10)

        self.player_sprite = pygame.sprite.GroupSingle(self.player)

        ### w space invaders nie można oddać kolejnego strzału dopóki obecny w nic nie trafi/dojdzie do końca mapy
        ### dlatego będę używał jednego obiektu zamiast tworzyć przy każdym wystrzale

    def run(self):
        '''GameLoop here:'''
        self.input_handling()
        self.projectile.update()

        self.player_sprite.draw(screen)
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
            

if __name__ == '__main__':
    # Window managment:
    pygame.init()
    screen_size = 800
    screen = pygame.display.set_mode((screen_size, screen_size))
    # Window Details
    pygame.display.set_caption("Space Invader")
    icon = pygame.image.load('ufo.png') 
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


        