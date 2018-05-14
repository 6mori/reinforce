import pygame as pg
from pygame.sprite import Sprite
from .. import tools as t
from .. import constants as c

class Prop(Sprite):
    def __init__(self, x, y, kind, width=1, height=1):
        super().__init__()
        self.kind = kind
        self.image = pg.transform.scale(pg.image.load(t.kindOfProps[kind]['name']),
                                        (c.BRICK_WIDTH*width, c.BRICK_HEIGHT*height))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.dur = c.BRICK_DUR


    def ActOnCharacters(self, character):
        if self.kind == 'red_prop':
            character.HP = character.HP+1
        elif self.kind == 'blue_prop':
            character.MP = character.MP+1
