import pygame as pg
from pygame.sprite import Sprite

from .. import tools
from .. import constants as c

class Character(Sprite):

    def __init__(self):
        super().__init__()
        #大招次数  默认为3
        self.MP = 3

        #默认贴图为Darling
        self.setup_character_image_initial(c.DARING)
        self.player_num = 0

        self.state = c.STANDING

        self.commands = {
            c.ACTION  : False,
            c.SKILL   : False,
            c.JUMP    : False,
            c.GO_LEFT : False,
            c.GO_RIGHT: False,
            c.GO_DOWN : False
        }

        self.setup_forces()
        self.setup_state_booleans()

        self.HP = 0

        self.walk_counter=0
        self.skill_counter=0


    def setup_character_image_initial(self,character_name):
        self.image = pg.transform.scale(pg.image.load('images/'+character_name+'/stand/0.png'), c.CHARACTER_SIZE)
        self.image_right = self.image
        self.image_left = pg.transform.flip(self.image_right, True, False)
        self.rect = self.image.get_rect()


    def setup_character_image_stand(self, character_name):
        self.image_right = pg.transform.scale(pg.image.load('images/'+character_name+'/stand/0.png'), c.CHARACTER_SIZE)
        self.image_left = pg.transform.flip(self.image_right, True, False)


    def setup_character_image_walk(self, character_name,max_frame_number):
        image_address = 'images/'+character_name+'/walk/%d.png' % (self.walk_counter // c.CHARACTER_MOVING_SPEED)
        self.walk_counter += 1
        self.walk_counter %= max_frame_number * c.CHARACTER_MOVING_SPEED
        self.image_right = pg.transform.scale(pg.image.load(image_address), c.CHARACTER_SIZE)
        self.image_left = pg.transform.flip(self.image_right, True, False)


    def setup_state_booleans(self):
        self.facing_right = True
        self.allow_jump = True
        self.allow_action = True
        self.allow_skill = True
        self.dead = False


    def setup_forces(self):
        self.x_vel = 0
        self.y_vel = 0
        self.max_x_vel = c.MAX_X_VEL
        self.max_y_vel = c.MAX_Y_VEL
        self.jump_vel = c.JUMP_VEL
        self.gravity = c.GRAVITY


    def update(self, keys, keybinding, game_info, action_group):
        self.bind_keys(keys, keybinding)
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state(action_group)
        self.character_direction()


    def character_direction(self):
        if self.facing_right:
            self.image = self.image_right
        else:
            self.image = self.image_left


    def bind_keys(self, keys, keybinding):
        for command in self.commands.keys():
            if keys[keybinding[command]]:
                self.commands[command] = True
            else:
                self.commands[command] = False


    def handle_state(self, action_group):
        if self.state == c.STANDING:
            self.stand(action_group)
        elif self.state == c.WALKING:
            self.walk(action_group)
        elif self.state == c.JUMPING:
            self.jump(action_group)
        elif self.state == c.FALLING:
            self.fall(action_group)
        elif self.state == c.SKILLING:
            self.skill(action_group)


    def stand(self, action_group):
        self.check_to_allow_jump()
        self.check_to_allow_action()
        self.check_to_allow_skill()

        self.setup_character_image_stand(c.DARING)

        self.x_vel = 0
        self.y_vel = 0

        if self.commands[c.ACTION]:
            if self.allow_action:
                self.action(action_group)

        if self.commands[c.SKILL]:
            if self.allow_skill:
                self.state = c.SKILLING
                return

        if self.commands[c.GO_LEFT]:
            self.facing_right = False
            self.state = c.WALKING
            self.x_vel = -self.max_x_vel
        elif self.commands[c.GO_RIGHT]:
            self.facing_right = True
            self.state = c.WALKING
            self.x_vel = self.max_x_vel
        elif self.commands[c.JUMP]:
            if self.allow_jump:
                self.state = c.JUMPING
                self.y_vel = self.jump_vel
        else:
            self.state = c.STANDING


    def walk(self, action_group):
        self.check_to_allow_jump()
        self.check_to_allow_action()
        self.check_to_allow_skill()

        #加载贴图
        self.setup_character_image_walk(c.DARING,4)

        if self.commands[c.ACTION]:
            if self.allow_action:
                self.action(action_group)

        if self.commands[c.SKILL]:
            if self.allow_skill:
                self.state = c.SKILLING

        if self.commands[c.JUMP]:
            if self.allow_jump:
                self.state = c.JUMPING
                self.y_vel = self.jump_vel

        if self.commands[c.GO_LEFT]:

            self.facing_right = False
            if self.x_vel >= 0:
                self.x_vel = -self.max_x_vel
            else:
                self.x_vel = 0

        elif self.commands[c.GO_RIGHT]:

            self.facing_right = True
            if self.x_vel <= 0:
                self.x_vel = self.max_x_vel
            else:
                self.x_vel = 0

        else:
            if self.y_vel == 0:
                self.state = c.STANDING
            self.x_vel = 0


    def jump(self, action_group):
        self.check_to_allow_action()
        self.check_to_allow_skill()

        self.allow_jump = False
        self.gravity = c.JUMP_GRAVITY
        self.y_vel += self.gravity

        if self.y_vel >= 0 and self.y_vel < self.max_y_vel:
            self.gravity = c.GRAVITY
            self.state = c.FALLING

        if self.commands[c.ACTION]:
            if self.allow_action:
                self.action(action_group)

        if self.commands[c.SKILL]:
            if self.allow_skill:
                self.state = c.SKILLING
                return

        if self.commands[c.GO_LEFT]:
            self.facing_right = False
            self.x_vel = -self.max_x_vel
        elif self.commands[c.GO_RIGHT]:
            self.facing_right = True
            self.x_vel = self.max_x_vel

        if not self.commands[c.JUMP]:
            self.gravity = c.GRAVITY
            self.state = c.FALLING


    def fall(self, action_group):
        self.check_to_allow_action()
        self.check_to_allow_skill()

        if self.y_vel < c.MAX_Y_VEL:
            self.y_vel += self.gravity

        if self.commands[c.ACTION]:
            if self.allow_action:
                self.action(action_group)

        if self.commands[c.SKILL]:
            if self.allow_skill:
                self.state = c.SKILLING

        if self.commands[c.GO_LEFT]:
            self.facing_right = False
            self.x_vel = -self.max_x_vel
        elif self.commands[c.GO_RIGHT]:
            self.facing_right = True
            self.x_vel = self.max_x_vel


    def action(self, action_group):
        pass


    def skill(self):
        pass


    def check_to_allow_jump(self):
        if not self.commands[c.JUMP]:
            self.allow_jump = True


    def check_to_allow_action(self):
        if not self.commands[c.ACTION]:
            self.allow_action = True


    def check_to_allow_skill(self):
        if (not self.commands[c.SKILL]) and (self.MP>0):
            self.allow_skill = True


    #def blitme(self):
    #    self.screen.blit( self.image, self.rect )

