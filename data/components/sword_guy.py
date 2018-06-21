import pygame as pg

from .. import constants as c
from . import character
from . import sword


class SwordGuy(character.Character):
    def __init__(self):
        super(SwordGuy, self).__init__()

        self.sword_damage = c.SWORD_DAMAGE
        self.HP = 10


    def action(self, action_group,character_name,frame_nums,postfix,size=None):
        super().action(character_name,frame_nums,postfix,size)
        if self.action_counter == 1:
            cutting_sword = sword.Sword(self.player_num, self.sword_damage)
            if self.facing_right:
                cutting_sword.rect.left = self.rect.right + c.MAX_X_VEL
            else:
                cutting_sword.rect.right = self.rect.left - c.MAX_X_VEL

            cutting_sword.damage = 100
            cutting_sword.rect.centery = self.rect.centery
            action_group.add(cutting_sword)

