import pygame, sys, random
from player import Player
from bullet import Bullet
from alien import Alien
from config import scale

class Game:
    def __init__(self,screen_size):
        #General
        self.font = pygame.font.Font('Pixeboy.ttf', 40)
        self.points = 0
        #Player
        self.player_sprite = Player(screen_size)
        self.player = pygame.sprite.GroupSingle(self.player_sprite)

        #zmiana planow

        #Aliens
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 5, cols = 11)
        self.alien_direction = 1
        self.enemy_lasers = pygame.sprite.Group()

    def score(self):
        score_text = self.font.render(f'score: {self.points}', False,'white')
        score_box = score_text.get_rect(topleft = (15,15))
        screen.blit(score_text, score_box)

    def alien_update(self):
        self.aliens.update(self.alien_direction, speed = 1)
        self.aliens.draw(screen)

        self.alien_bounce()
        
        self.enemy_lasers.draw(screen)
        self.enemy_lasers.update()

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
            
    def alien_bounce(self):
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

    def alien_shoot(self):
        if self.aliens.sprites():
            shooter = random.choice(self.aliens.sprites())
            laser = Bullet(-3, shooter.rect.center)
            self.enemy_lasers.add(laser)
    
    def collision_check(self):
        if self.player.sprite.bulletGroup:
            for bullet in self.player.sprite.bulletGroup:
                if pygame.sprite.spritecollide(bullet, self.aliens, True):
                    self.points += 100
                    self.player_sprite.bullet.destroy()
        if self.enemy_lasers:
            for laser in self.enemy_lasers:
                if pygame.sprite.spritecollide(laser, self.player, False):
                    self.points -= 50
                    if self.points < 0:
                        self.points = 0
                    laser.kill()

    def run(self):
        '''GameLoop here:'''
        self.alien_update()
        self.player.update()
        self.score()



        self.player.draw(screen)
        self.player.sprite.bulletGroup.draw(screen)
        self.collision_check()

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

    alienshot = pygame.USEREVENT
    pygame.time.set_timer(alienshot,1000)
    while True:
        screen.fill((0, 0, 0))
        #KeyCheck
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == alienshot:
                game.alien_shoot()
        game.run()
        pygame.display.flip()
        clock.tick(60)


        