import pygame
from pygame.sprite import Sprite

from settings import Settings

class Brick(Sprite):

    def __init__( self, x_count, y_count, settings, screen ):
        super().__init__()
        #self.screen = screen
        self.x_count = x_count
        self.y_count = y_count
        self.width = settings.brick_width
        self.height = settings.brick_height

        #self.image = pygame.image.load('images/')
        #self.rect = self.image.get_rect()
        self.rect = pygame.Rect( ( x_count*self.width, y_count*self.height ), ( self.width, self.height ) )
        self.screen_rect = screen.get_rect()

        self.durability = 0

        # for test
        self.screen = screen
        self.color = (226, 43, 48)

    #def update(self):
    def blitme(self):
        self.screen.blit( self.image, self.rect )

    # for test
    def draw(self):
        pygame.draw.rect( self.screen, self.color, self.rect )