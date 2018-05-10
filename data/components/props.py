import pygame as pg
from pygame.sprite import Sprite
from .. import constants as c

class RedItem(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load('images/prop_red.png'), (c.BRICK_WIDTH, c.BRICK_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.dur = c.BRICK_DUR

class BlueItem(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load('images/prop_blue.png'), (c.BRICK_WIDTH, c.BRICK_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.dur = c.BRICK_DUR

