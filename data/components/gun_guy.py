from .. import constants as c
from . import character
from . import bullet
import pygame as pg


class GunGuy(character.Character):
    def __init__(self):
        super().__init__()

        self.bullet_damage = c.BULLET_DAMAGE
        self.HP = 10

    def get_bullet_type(self, character_name, direction):
        # 默认为Darling
        if character_name == c.DARLING:
            if self.player_num == 0:
                return bullet.Bullet(self.player_num, self.bullet_damage, direction, 'flamebow')
            else:
                return bullet.Bullet(self.player_num, self.bullet_damage, direction, 'freezebow')
        elif character_name == c.SPIDER_PRINCE:
            if self.player_num == 0:
                return bullet.Bullet(self.player_num, self.bullet_damage, direction, 'flamebow')
            else:
                return bullet.Bullet(self.player_num, self.bullet_damage, direction, 'freezebow')
        else:  # 默认为Darling
            if self.player_num == 0:
                return bullet.Bullet(self.player_num, self.bullet_damage, direction, 'flamebow')
            else:
                return bullet.Bullet(self.player_num, self.bullet_damage, direction, 'freezebow')

    def handle_bullet_direction(self, Mybullet):
        if self.facing_right:
            Mybullet.x_vel = c.BULLET_VEL
            Mybullet.rect.left = self.rect.right
        else:
            Mybullet.x_vel = -c.BULLET_VEL
            Mybullet.rect.right = self.rect.left
