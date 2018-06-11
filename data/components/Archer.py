from . import gun_guy
from .. import constants as c

class Archer(gun_guy.GunGuy):
    def __init__(self):
        super().__init__()

        self.bullet_damage = 5
        self.HP = 25
        self.MP = 3

    # 大招
    def skill(self, action_group):
        self.skill_basic_operation_front('Archer', 1, 'png')
        self.wild_shot_bullets(action_group)
        self.skill_basic_operation_back('Archer', 1)

    # 发射弓箭
    def action(self, action_group):
        self.allow_action = False
        #弓箭方向
        if self.facing_right:
            firing_arrow = self.get_bullet_type(c.ARCHER, c.RIGHT)
        else:
            firing_arrow = self.get_bullet_type(c.ARCHER, c.LEFT)
        #弓箭方向
        self.handle_bullet_direction(firing_arrow)
        #弓箭发射位置
        firing_arrow.rect.top = self.rect.top
        #弓箭组
        action_group.add(firing_arrow)

    def setup_character_image_initial(self, character_name, postfix):
        super().setup_character_image_initial(c.ARCHER, 'png')

    def setup_character_image_stand(self, character_name,max_frame_number,postfix):
        super().setup_character_image_stand(c.ARCHER, 1, 'png')

    def setup_character_image_walk(self, character_name,max_frame_number,postfix):
        super().setup_character_image_walk(c.ARCHER, 2, 'png')

    def wild_shot_bullets(self, action_group):
        if not self.skill_counter % (c.SKILL_SPEED['Archer'] * 2):
            if self.facing_right:
                arrows = [self.get_bullet_type(c.ARCHER, c.RIGHT),
                          self.get_bullet_type(c.ARCHER, c.RIGHT),
                          self.get_bullet_type(c.ARCHER, c.RIGHT)]
            else:
                arrows = [self.get_bullet_type(c.ARCHER, c.LEFT),
                          self.get_bullet_type(c.ARCHER, c.LEFT),
                          self.get_bullet_type(c.ARCHER, c.LEFT)]
            if self.facing_right:
                arrows[0].rect.y = self.rect.y
                arrows[1].rect.y = self.rect.y - 15
                arrows[2].rect.y = self.rect.y + 15
                for i in range(0, 3):
                    arrows[i].rect.right = self.rect.right
                    arrows[i].rect.x = self.rect.x
                    arrows[i].x_vel = c.BULLET_VEL * 2
            else:
                arrows[0].rect.y = self.rect.y
                arrows[1].rect.y = self.rect.y - 15
                arrows[2].rect.y = self.rect.y + 15
                for i in range(0, 3):
                    arrows[i].rect.left = self.rect.left
                    arrows[i].rect.x = self.rect.x
                    arrows[i].x_vel = -c.BULLET_VEL * 2
            for i in range(0, 3):
                action_group.add(arrows[i])