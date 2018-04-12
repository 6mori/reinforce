import pygame as pg
from pygame.sprite import Sprite

from .. import constants as c

class Bullet(Sprite):
    def __init__(self, owner, damage):
        super().__init__()

        self.rect = pg.Rect((0, 0), (c.BULLET_WIDTH, c.BULLET_HEIGHT))
        self.owner = owner
        self.damage = damage
        self.x_vel = 0

        # For test
        self.color = c.BLUE

    def update(self):
        self.rect.x += round(self.x_vel)
