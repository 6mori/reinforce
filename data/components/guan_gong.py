from . import sword_guy
from .. import constants as c
class Guan_gong(sword_guy.SwordGuy):
    def __init__(self):
        super().__init__()

        self.sword_damage = 5
        self.HP = 10


    def skill(self, action_group):

        self.skill_basic_operation_front(c.GUAN_GONG,10,'gif')
        #冲刺
        if self.facing_right:
            self.rect.x += 6
        else:
            self.rect.x -= 6
        self.skill_basic_operation_back(c.GUAN_GONG,10)


    def setup_character_image_initial(self, character_name, postfix):
        super().setup_character_image_initial(c.GUAN_GONG,'gif')


    def setup_character_image_stand(self, character_name,frame_number,postfix):
        super().setup_character_image_stand(c.GUAN_GONG,7,'gif')


    def setup_character_image_walk(self, character_name,frame_number,postfix):
        super().setup_character_image_walk(c.GUAN_GONG,6,'png')