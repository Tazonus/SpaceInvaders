import pygame, sys
from player import Player

class Game:
    def __init__(self):
        Player_sprite = Player((screen_width/2 ,screen_height * 99/100),64)
        self.player = pygame.sprite.GroupSingle(Player_sprite)

    def run(self):
        '''GameLoop here:'''
        self.player.update()
        self.player.draw(screen)
        #update all sprite groups
        #draw all sprite groups

if __name__ == '__main__':
    # Window managment:
    pygame.init()
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Window Details
    pygame.display.set_caption("Space Invader")
    icon = pygame.image.load('ufo.png') 
    pygame.display.set_icon(icon)

    # Logic and time
    game = Game()
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


        