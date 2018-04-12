
from .. import constants as c
from . import character
from . import bullet

class Gun_guy(character.Character):
    def __init__(self):
        super(Gun_guy, self).__init__()

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
        firing_bullet.rect.y = self.rect.y
        action_group.add(firing_bullet)
