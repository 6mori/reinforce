import pygame as pg
from pygame.sprite import Group

from .. import tools, setup
from .. import constants as c
from .. components import brick, character


class gaming(tools._State):
    def __init__(self):
        super(gaming, self).__init__()

    #def get_event(self, event):

    def startup(self, current_time, persist):
        self.game_info = persist
        self.persist = self.game_info
        self.game_info[c.CURRENT_TIME] = current_time

        self.setup_bricks()
        self.setup_character()
        #self.setup_spritegroups()


    def setup_bricks(self):
        self.bricks_group = Group()
        self.creat_bricks(self.bricks_group, 0, 20, 80, 1)
        self.creat_bricks(self.bricks_group, 35, 0, 1, 15)
        self.creat_bricks(self.bricks_group, 35, 20, 1, 10)
        self.creat_bricks(self.bricks_group, 0, 15, 30, 1)


    def creat_bricks(self, bricks, x, y, width, height):
        for row in list(range(x, x+width)):
            for col in list(range(y, y+height)):
                self.creat_brick(bricks, row, col)


    def creat_brick(self, bricks, row, col):
        x = row * c.BRICK_WIDTH
        y = col * c.BRICK_HEIGHT

        bricks.add(brick.Brick(x, y))


    def setup_character(self):
        self.character = character.Character()
        self.character.rect.x = 0
        self.character.rect.y = 0
        self.character.state = c.FALL


    def update(self, surface, keys, current_time):
        self.game_info[c.CURRENT_TIME] = self.current_time = current_time
        self.handle_state(keys)
        self.blit_everything(surface)


    def handle_state(self, keys):
        self.update_all_sprites(keys)


    def update_all_sprites(self, keys):
        self.character.update(keys, self.game_info)
        self.adjust_sprite_positions()


    def adjust_sprite_positions(self):
        self.adjust_character_positions()


    def adjust_character_positions(self):
        self.character.rect.x += round(self.character.x_vel)
        self.check_character_x_collisions()

        self.character.rect.y += round(self.character.y_vel)
        self.check_character_y_collisions()


    def check_character_x_collisions(self):
        brick = pg.sprite.spritecollideany(self.character, self.bricks_group)

        if brick:
            self.adjust_character_for_x_collisions(brick)


    def adjust_character_for_x_collisions(self, collider):
        if self.character.rect.x < collider.rect.x:
            self.character.rect.right = collider.rect.left
        else:
            self.character.rect.left = collider.rect.right

        self.character.x_vel = 0


    def check_character_y_collisions(self):
        brick = pg.sprite.spritecollideany(self.character, self.bricks_group)

        if brick:
            self.adjust_character_for_y_collisions(brick)

        self.check_if_character_is_falling()


    def adjust_character_for_y_collisions(self, collider):
        print(self.character.rect.y, collider.rect.y)
        if self.character.rect.y < collider.rect.y:
            self.character.rect.bottom = collider.rect.top
            self.character.state = c.WALK
        else:
            self.character.rect.top = collider.rect.bottom

        self.character.y_vel = 0


    def check_if_character_is_falling(self):
        self.character.rect.y += 1
        test_collide_group = pg.sprite.Group(self.bricks_group)

        if pg.sprite.spritecollideany(self.character, test_collide_group) is None:
                if self.character.state != c.JUMP:
                    self.character.state = c.FALL
        self.character.rect.y -= 1


    def blit_everything(self, surface):
        # For test
        surface.fill(c.BG_COLOR)
        pg.draw.rect(surface, self.character.color, self.character.rect)
        for brick in self.bricks_group.sprites():
            pg.draw.rect(surface, brick.color, brick.rect)

