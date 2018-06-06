from . import bullet
import pygame as pg
class Skill_attack(bullet.Bullet):
    def __init__(self, owner, damage, direction, bullet_style,size):
        super().__init__(owner,damage,direction,bullet_style)

        self.image = pg.transform.scale(pg.image.load('images/bullet/' + bullet_style + '/0.png'), size)
