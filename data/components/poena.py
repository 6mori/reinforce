from . import sword_guy
from .. import constants as c

class Poena(sword_guy.SwordGuy):
    def __init__(self):
        super().__init__()

        self.sword_damage = 5
        self.HP = 10


    def skill(self, action_group):

        self.skill_basic_operation_front(c.POENA,6,'png',(40, 65))


        self.skill_basic_operation_back(c.POENA,6)


    def setup_character_image_initial(self, character_name, postfix):
        super().setup_character_image_initial(c.POENA,'png')


    def setup_character_image_stand(self, character_name,frame_number,postfix):
        super().setup_character_image_stand(c.POENA,3,'png')


    def setup_character_image_walk(self, character_name,frame_number,postfix):
        super().setup_character_image_walk(c.POENA,6,'png')