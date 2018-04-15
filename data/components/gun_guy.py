
from .. import constants as c
from . import character
from . import bullet
import pygame as pg

class Gun_guy(character.Character):
    def __init__(self,screen):
        super(Gun_guy, self).__init__(screen)

        self.bullet_damage = c.P1_DAMAGE

        self.HP = 10


    def action(self, action_group):
        self.allow_action = False

        firing_bullet = bullet.Bullet(self.name, self.bullet_damage)
        if self.facing_right:
            firing_bullet.x_vel = c.BULLET_VEL
            firing_bullet.rect.left = self.rect.right
        else:
            firing_bullet.x_vel = -c.BULLET_VEL
            firing_bullet.rect.right = self.rect.left
        firing_bullet.rect.centery = self.rect.centery
        action_group.add(firing_bullet)

    def skill(self):
        self.allow_skill = False

        # self.skill_animation()
        image_address = 'images/dnf_r_%d.png' % (self.skill_counter // c.CHARACTER_SKILL_SPEED)
        self.skill_counter += 1
        self.skill_counter %= 16 * c.CHARACTER_SKILL_SPEED
        self.image_right = pg.transform.scale(pg.image.load(image_address), c.CHARACTER_SIZE)
        self.image_left = pg.transform.flip(self.image_right, True, False)

        if self.skill_counter == 16 * c.CHARACTER_SKILL_SPEED-1:
            self.state = c.WALK




    def skill_animation(self):
        for i in range(16*c.CHARACTER_SKILL_SPEED):
            image_address = 'images/dnf_r_%d.png' % (self.skill_counter // c.CHARACTER_SKILL_SPEED)
            self.skill_counter += 1
            self.skill_counter %= 16*c.CHARACTER_SKILL_SPEED

            self.image_right = pg.transform.scale(pg.image.load(image_address), c.CHARACTER_SIZE)
            self.image_left = pg.transform.flip(self.image_right, True, False)
            self.blitme()
            self.image_left = pg.transform.flip(self.image_right, True, False)
