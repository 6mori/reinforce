import pygame as pg
from pygame.sprite import Sprite
from .. import tools as t
from .. import constants as c

class Brick(Sprite):

    def __init__(self, x, y,kind,width=1,height=1):#width和height为砖块长宽
        super().__init__()
        #self.rect = pg.Rect((x, y), (c.BRICK_WIDTH, c.BRICK_HEIGHT))

        self.image =  pg.transform.scale(pg.image.load(t.kindOfBrick[kind]['name']),(c.BRICK_WIDTH*width,c.BRICK_HEIGHT*height))
        self.rect = self.image.get_rect()
        #self.rect.width=x
        #self.rect.bottom=y
        self.rect.left = x
        self.rect.top = y

        self.HP = c.BRICK_DUR

        # for test
        self.color = c.ORANGE

    #def update(self):
    def blitme(self,screen):
        screen.blit( self.image, self.rect )

    # for test