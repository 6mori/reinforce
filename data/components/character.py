import pygame as pg
from pygame.sprite import Sprite

from .. import tools
from .. import constants as c

class Character(Sprite):

    def __init__(self):
        super().__init__()

        #self.image = pygame.image.load('images/')
        #self.rect = self.image.get_rect()
        self.state = c.STAND

        self.setup_forces()
        self.setup_state_booleans()

        # For test
        self.rect = pg.Rect((0, 0), (c.WIDTH, c.HEIGHT))
        self.color = c.RED


    def setup_state_booleans(self):
        self.facing_right = True
        self.allow_jump = True
        self.dead = False
        self.in_transition_state = False


    def setup_forces(self):
        self.x_vel = 0
        self.y_vel = 0
        self.max_x_vel = c.MAX_X_VEL
        self.max_y_vel = c.MAX_Y_VEL
        self.jump_vel = c.JUMP_VEL
        self.gravity = c.GRAVITY


    def update(self, keys, game_info):
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state(keys)
        #self.check_for_special_state()
        #self.animation()


    def handle_state(self, keys):
        if self.state == c.STAND:
            self.stand(keys)
        elif self.state == c.WALK:
            self.walk(keys)
        elif self.state == c.JUMP:
            self.jump(keys)
        elif self.state == c.FALL:
            self.fall(keys)


    def stand(self, keys):
        self.check_to_allow_jump(keys)

        self.x_vel = 0
        self.y_vel = 0

        if keys[tools.keybinding['left']]:
            self.facing_right = False
            self.state = c.WALK
            self.x_vel = -self.max_x_vel
        elif keys[tools.keybinding['right']]:
            self.facing_right = True
            self.state = c.WALK
            self.x_vel = self.max_x_vel
        elif keys[tools.keybinding['jump']]:
            if self.allow_jump:
                self.state = c.JUMP
                self.y_vel = self.jump_vel
        else:
            self.state = c.STAND


    def walk(self, keys):
        self.check_to_allow_jump(keys)

        if keys[tools.keybinding['jump']]:
            if self.allow_jump:
                self.state = c.JUMP
                self.y_vel = self.jump_vel

        if keys[tools.keybinding['left']]:
            self.facing_right = False
            if self.x_vel >= 0:
                self.x_vel = -self.max_x_vel
            else:
                self.x_vel = 0

        elif keys[tools.keybinding['right']]:
            self.facing_right = True
            if self.x_vel <= 0:
                self.x_vel = self.max_x_vel
            else:
                self.x_vel = 0



        else:
            if self.y_vel == 0:
                self.state = c.STAND
            self.x_vel = 0

    def jump(self, keys):
        self.allow_jump = False
        self.gravity = c.JUMP_GRAVITY
        self.y_vel += self.gravity

        if self.y_vel >= 0 and self.y_vel < self.max_y_vel:
            self.gravity = c.GRAVITY
            self.state = c.FALL

        if keys[tools.keybinding['left']]:
            self.facing_right = False
            self.x_vel = -self.max_x_vel
        elif keys[tools.keybinding['right']]:
            self.facing_right = True
            self.x_vel = self.max_x_vel

        if not keys[tools.keybinding['jump']]:
            self.gravity = c.GRAVITY
            self.state = c.FALL


    def fall(self, keys):
        if self.y_vel < c.MAX_Y_VEL:
            self.y_vel += self.gravity


    def check_to_allow_jump(self, keys):
        if not keys[tools.keybinding['jump']]:
            self.allow_jump = True

        if keys[tools.keybinding['left']]:
            self.facing_right = False
            self.x_vel = self.max_x_vel
        elif keys[tools.keybinding['right']]:
            self.facing_right = True
            self.x_vel = -self.max_x_vel


    def blitme(self):
        self.screen.blit( self.image, self.rect )

    # for test
