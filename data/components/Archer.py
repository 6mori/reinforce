from . import gun_guy
from .. import constants as c
from . import skill_attack


class Archer(gun_guy.GunGuy):
    def __init__(self):
        super().__init__()

        self.bullet_damage = 5
        self.HP = 25
        self.MP = 3
        self.name = c.ARCHER

    # 大招
    def skill(self, action_group):
        super().skill('Archer', 1, 'gif')
        if self.skill_counter == 1:
            if self.facing_right:
                attack = skill_attack.Skill_attack(self.player_num, 100, c.RIGHT, 'dodge',
                                                   c.ARCHER)
                attack.rect.left = self.rect.right
                attack.x_vel = c.BULLET_VEL // 2
            else:
                attack = skill_attack.Skill_attack(self.player_num, 100, c.LEFT, 'dodge',
                                                   c.ARCHER)
                attack.rect.right = self.rect.left
                attack.x_vel = -c.BULLET_VEL // 2
            attack.rect.centery = self.rect.top
            attack.penetration_mode = 3  # 全穿透
            action_group.add(attack)

    # 发射弓箭
    def action(self, action_group):
        self.allow_action = False
        # 弓箭方向
        if self.facing_right:
            firing_arrow = self.get_bullet_type(c.ARCHER, c.RIGHT)
        else:
            firing_arrow = self.get_bullet_type(c.ARCHER, c.LEFT)
        # 弓箭方向
        self.handle_bullet_direction(firing_arrow)
        # 弓箭发射位置
        firing_arrow.rect.top = self.rect.top
        # 弓箭组
        action_group.add(firing_arrow)

    def setup_character_image_initial(self, character_name, postfix):
        super().setup_character_image_initial(c.ARCHER, 'gif')

    def setup_character_image_stand(self, character_name, max_frame_number, postfix):
        super().setup_character_image_stand(c.ARCHER, 1, 'gif')

    def setup_character_image_walk(self, character_name, max_frame_number, postfix):
        super().setup_character_image_walk(c.ARCHER, 2, 'gif')
