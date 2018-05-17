from . import sword_guy
from .. import constants as c
class K(sword_guy.SwordGuy):
    def __init__(self):
        super().__init__()

        self.sword_damage = 5
        self.HP = 10

    def skill(self, action_group):

        self.skill_basic_operation_front(c.K,21,'gif')
        #冲刺

        self.skill_basic_operation_back(c.K,21,'gif')

    def setup_character_image_initial(self, character_name, postfix):
        super().setup_character_image_initial(c.K,'gif')

    def setup_character_image_stand(self, character_name,frame_number,postfix):
        super().setup_character_image_stand(c.K,40,'gif')

    def setup_character_image_walk(self, character_name,frame_number,postfix):
        super().setup_character_image_walk(c.K,8,'gif')