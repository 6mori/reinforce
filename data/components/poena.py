from . import sword_guy
from .. import constants as c
from . import skill_attack

class Poena(sword_guy.SwordGuy):
    def __init__(self):
        super().__init__()

        self.sword_damage = 5
        self.HP = 10


    def skill(self, action_group):

        self.skill_basic_operation_front(c.POENA,5,'png',(107//3, 111//3))
        if self.skill_counter == 1:
            if self.facing_right:
                attack = skill_attack.Skill_attack(self.player_num, 200, c.RIGHT, 'cross',
                                                   c.POENA)
                attack.rect.left = self.rect.right
                attack.x_vel = 4
            else:
                attack = skill_attack.Skill_attack(self.player_num, 200, c.LEFT, 'cross',
                                                   c.POENA)
                attack.rect.right = self.rect.left
                attack.x_vel = -4
            attack.rect.bottom = self.rect.bottom
            action_group.add(attack)

        self.skill_basic_operation_back(c.POENA,5)


    def setup_character_image_initial(self, character_name, postfix):
        super().setup_character_image_initial(c.POENA,'png')


    def setup_character_image_stand(self, character_name,frame_number,postfix):
        super().setup_character_image_stand(c.POENA,3,'png')


    def setup_character_image_walk(self, character_name,frame_number,postfix):
        super().setup_character_image_walk(c.POENA,6,'png')