import pygame as pg
from pygame.sprite import Sprite
from .. import tools as t
from .. import constants as c


class Brick(Sprite):

    def __init__(self, x, y, kind, width=1, height=1):  # width和height为砖块长宽
        super().__init__()
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.kind=kind
        self.counter=0
        self.HP = t.kindOfBrick[kind]['dur']
        if t.kindOfBrick[kind]['movable']:
            self.max_frame = t.kindOfBrick[self.kind]['frame']
            self.image = pg.transform.scale(pg.image.load(t.kindOfBrick[self.kind]['name'] + '%d.png' % (self.counter // c.MOVING_BRICK_SPEED)).convert(),(c.BRICK_WIDTH * self.width, c.BRICK_HEIGHT * self.height))
        else:
            self.image = pg.transform.scale(pg.image.load(t.kindOfBrick[self.kind]['name'] + '.png').convert(),(c.BRICK_WIDTH * self.width, c.BRICK_HEIGHT * self.height))

        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y
        self.vincible = True
        # for test
        self.color = c.ORANGE
        self.update()

    def update(self):
        if t.kindOfBrick[self.kind]['movable']:
                self.image = pg.transform.scale(pg.image.load(t.kindOfBrick[self.kind]['name']+'%d.png' % (self.counter//c.MOVING_BRICK_SPEED)).convert(),(c.BRICK_WIDTH * self.width, c.BRICK_HEIGHT * self.height))
                self.counter+=1
                self.counter%=self.max_frame*c.MOVING_BRICK_SPEED
        else:
            pass
    # def update(self):
    # def blitme(self,screen):
    #    screen.blit( self.image, self.rect )

    # for test
    def ActOnCharacter(self,character):
        if self.kind=='fire':
            character.HP -= c.FIRE_BRICK_DAMAGE