import pygame as pg
from pygame.sprite import Sprite

from .. import constants as c

class Sword(Sprite):
    def __init__(self, owner, damage):
        super().__init__()

        # self.rect = pg.Rect((0, 0), (c.SWORD_WIDTH, c.SWORD_HEIGHT))
        self.owner = owner
        self.damage = damage
        self.creat_time = 0.0
        self.is_finished = False

        self.image = pg.transform.scale(pg.image.load('images/sword.png'), (50,20))
        self.rect = self.image.get_rect()
        # For test
        self.color = c.BLUE

    def update(self):
        pass

