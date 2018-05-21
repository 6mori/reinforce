
from .. import constants as c
from . import character
from . import bullet
import pygame as pg

class GunGuy(character.Character):
    def __init__(self):
        super().__init__()

        self.bullet_damage = c.P1_DAMAGE
        self.HP = 10


    def action(self, action_group):
        self.allow_action = False
        # 子弹类型
        if self.facing_right:
            firing_bullet = self.get_bullet_type(c.DARING, c.RIGHT)
        else:
            firing_bullet = self.get_bullet_type(c.DARING, c.LEFT)
        # 子弹方向
        self.handle_bullet_direction(firing_bullet)
        # 子弹发射位置
        firing_bullet.rect.centery = self.rect.centery - 23
        # 子弹组
        action_group.add(firing_bullet)


    def skill(self, action_group):
        pass


    def get_bullet_type(self,character_name,direction):
        #默认为Darling
        if character_name == c.DARLING:
            if self.player_num == 0:
                return bullet.Bullet(self.player_num, self.bullet_damage, direction, 'flamebow')
            else:
                return bullet.Bullet(self.player_num, self.bullet_damage, direction, 'freezebow')


    def handle_bullet_direction(self,Mybullet):
        if self.facing_right:
            Mybullet.x_vel = c.BULLET_VEL
            Mybullet.rect.left = self.rect.right
        else:
            Mybullet.x_vel = -c.BULLET_VEL
            Mybullet.rect.right = self.rect.left