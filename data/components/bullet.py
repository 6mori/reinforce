import pygame as pg
from pygame.sprite import Sprite

from .. import constants as c

class Bullet(Sprite):
    def __init__(self, owner, damage):
        super().__init__()

        #加载子弹图片并设置子弹大小

        self.image=pg.transform.scale(pg.image.load('images/bullet/1.png'),c.BULLET_SIZE)
        self.rect = self.image.get_rect()


        self.owner = owner
        self.damage = damage
        self.x_vel = 0



    def update(self):
        self.rect.x += round(self.x_vel)

    def blitme(self,screen):
        screen.blit(self.image, self.rect)
