from . import gun_guy
from .. import constants as c
from . import skill_attack


class Iccy(gun_guy.GunGuy):
    def __init__(self):
        super().__init__()

        self.bullet_damage = 50
        self.HP = 100
        self.MP = 3
        self.name = c.ICCY

    def skill(self, action_group):
        super().skill(c.ICCY, 11, 'gif')


    def action(self, action_group):
        super().action(c.ICCY, 8, 'gif')
        if self.action_counter == 1:
            # 子弹类型
            if self.facing_right:
                firing_bullet = self.get_bullet_type(c.SPIDER_PRINCE, c.RIGHT)
            else:
                firing_bullet = self.get_bullet_type(c.SPIDER_PRINCE, c.LEFT)
            # 子弹方向
            self.handle_bullet_direction(firing_bullet)
            # 子弹发射位置
            firing_bullet.rect.centery = self.rect.centery
            # 子弹组
            action_group.add(firing_bullet)

    def setup_character_image_initial(self, character_name, postfix):
        super().setup_character_image_initial(c.ICCY, 'gif')

    def setup_character_image_stand(self, character_name, max_frame_number, postfix):
        super().setup_character_image_stand(c.ICCY, 8, 'gif')

    def setup_character_image_walk(self, character_name, max_frame_number, postfix):
        super().setup_character_image_walk(c.ICCY, 8, 'gif')

