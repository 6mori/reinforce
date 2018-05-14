from . import gun_guy
from .. import constants as c
import pygame as pg

class Darling(gun_guy.GunGuy):
    def __init__(self):
        super().__init__()

        self.bullet_damage = 5
        self.HP = 10
        self.MP = 3

    def skill(self, action_group):
        self.allow_skill = False

        action_image_address = 'images/Darling/skill/action/dnf_r_%d.png' % (self.skill_counter // c.SKILL_SPEED_DARLING)
        #发射子弹
        self.wild_shot_bullets(action_group)

        self.skill_counter += 1
        self.skill_counter %= 16 * c.SKILL_SPEED_DARLING
        self.image_right = pg.transform.scale(pg.image.load(action_image_address), c.CHARACTER_SIZE)
        self.image_left = pg.transform.flip(self.image_right, True, False)


        if self.skill_counter == 16 * c.SKILL_SPEED_DARLING-1:
            self.state = c.FALLING
            self.MP -= 1

    def action(self, action_group):
        self.allow_action = False
        #子弹类型
        if self.facing_right:
            firing_bullet = self.get_bullet_type(c.DARING, c.RIGHT)
        else:
            firing_bullet = self.get_bullet_type(c.DARING, c.LEFT)
        #子弹方向
        self.handle_bullet_direction(firing_bullet)
        #子弹发射位置
        #firing_bullet.rect.centery = self.rect.centery-23
        firing_bullet.rect.top = self.rect.top
        #子弹组
        action_group.add(firing_bullet)

    def setup_character_image_initial(self,character_name):
        super().setup_character_image_initial(c.DARING)

    def setup_character_image_stand(self, character_name):
        super().setup_character_image_stand(c.DARING)

    def setup_character_image_walk(self, character_name,max_frame_number):
        super().setup_character_image_walk(c.DARING,5)

    def wild_shot_bullets(self,action_group):
        if not self.skill_counter%(c.SKILL_SPEED_DARLING*2):
            bullets = [self.get_bullet_type(c.DARING, c.LEFT), self.get_bullet_type(c.DARING, c.RIGHT),
                       self.get_bullet_type(c.DARING, c.UP), self.get_bullet_type(c.DARING, c.RIGHT_UP),
                       self.get_bullet_type(c.DARING, c.LEFT_UP)]
            bullets[0].x_vel = -c.BULLET_VEL
            bullets[4].x_vel = -c.BULLET_VEL
            bullets[1].x_vel = c.BULLET_VEL
            bullets[3].x_vel = c.BULLET_VEL
            bullets[2].y_vel = -c.BULLET_VEL
            bullets[3].y_vel = -c.BULLET_VEL
            bullets[4].y_vel = -c.BULLET_VEL

            bullets[1].rect.left = self.rect.right
            bullets[3].rect.left = self.rect.right
            bullets[2].rect.centerx = self.rect.centerx
            bullets[0].rect.right = self.rect.left
            bullets[4].rect.right = self.rect.left
            for i in range(len(bullets)):
                bullets[i].rect.centery = self.rect.centery - 23
                if i >= 2:
                    bullets[i].rect.bottom = self.rect.top
                action_group.add(bullets[i])

