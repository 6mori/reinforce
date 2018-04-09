import pygame
from pygame.sprite import Sprite

from settings import Settings

class Character(Sprite):

    def __init__( self, x, y, settings, screen ):
        super().__init__()

        self.x = x
        self.y = y
        self.width = settings.character_width
        self.height = settings.character_height
        #self.drop_speed = settings.character_drop_speed
        self.run_speed = settings.character_run_speed
        self.gravity_acceleration = settings.character_gravity_acceleration
        self.jumping_speed = settings.character_jumping_speed
        self.drop_speed = 0

        #self.image = pygame.image.load('images/')
        #self.rect = self.image.get_rect()
        self.rect = pygame.Rect( ( x-self.width/2, y-self.height/2), ( self.width, self.height ) )
        self.screen_rect = screen.get_rect()

        self.jumping = False
        self.not_on_land = True
        self.moving_left = False
        self.moving_right = False
        self.no_brick_on_left = True
        self.no_brick_on_right = True

        # for test
        self.screen = screen
        self.color = ( 226, 43, 48 )


    def update(self):
        if self.not_on_land == False:
            if self.jumping:
                self.drop_speed = self.jumping_speed
                self.jumping = False
                self.not_on_land = True
        if self.not_on_land:
            if self.jumping:
                self.jumping = False
            self.drop_speed += self.gravity_acceleration
            self.y += self.drop_speed
        if self.moving_left and self.no_brick_on_left and self.rect.left > 0:
            self.x -= self.run_speed
        if self.moving_right and self.no_brick_on_right and self.rect.right < self.screen_rect.right:
            self.x += self.run_speed
        self.rect.centerx = self.x
        self.rect.centery = self.y


    def blitme(self):
        self.screen.blit( self.image, self.rect )

    # for test
    def draw(self):
        pygame.draw.rect( self.screen, self.color, self.rect )