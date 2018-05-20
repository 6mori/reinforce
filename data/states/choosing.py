import pygame as pg

from .. import tools, setup
from .. import constants as c

class Choosing(tools._State):
    def __init__(self):
        super(Choosing, self).__init__()


    def startup(self, current_time, persist):
        self.game_info = persist
        self.persist = self.game_info

        self.next = c.GAMING

        self.setup_background()
        self.setup_cursor()


    def setup_background(self):
        self.background = pg.transform.scale(pg.image.load('images/%s.png' % c.CHOOSING_SCREEN), c.SCREEN_SIZE)
        self.background_rect = self.background.get_rect()


    def setup_cursor(self):
        self.cursor_1 = self.creat_cursor(c.P1_DARLING[1], 50, 50)
        self.cursor_1.state = c.P1_DARLING
        self.cursor_1.confirm = False

        self.cursor_2 = self.creat_cursor(c.P2_DARLING[1], 50, 50)
        self.cursor_2.state = c.P2_DARLING
        self.cursor_2.confirm = False


    def creat_cursor(self, pos, height, width):
        cursor = pg.sprite.Sprite()
        cursor.image = pg.Surface([height, width])
        # self.cursor.image.set_colorkey(c.BLACK)
        cursor.rect = cursor.image.get_rect()
        cursor.rect.x = pos[0]
        cursor.rect.y = pos[1]
        return cursor


    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.game_info[c.CURRENT_TIME] = self.current_time
        self.update_cursor()
        self.blit_everything(surface)
        self.check_if_all_confirmed()


    def get_event(self, event):
        P1_input_list = {
            pg.K_w: c.UP,
            pg.K_s: c.DOWN,
            pg.K_a: c.LEFT,
            pg.K_d: c.RIGHT,
            pg.K_RETURN: c.CONFIRM
        }
        P2_input_list = {
            pg.K_UP: c.UP,
            pg.K_DOWN: c.DOWN,
            pg.K_LEFT: c.LEFT,
            pg.K_RIGHT: c.RIGHT,
            pg.K_KP_ENTER: c.CONFIRM
        }

        if event.type == pg.KEYDOWN:
            if self.cursor_1.confirm == False:
                if event.key in P1_input_list.keys():
                    command = P1_input_list[event.key]
                    if command == c.CONFIRM:
                        self.cursor_1.confirm = True
                    next_state = c.CHOOSING_POSITION[self.cursor_1.state].get(command)
                    if next_state:
                        self.cursor_1.state = next_state

            if self.cursor_2.confirm == False:
                if event.key in P2_input_list.keys():
                    command = P2_input_list[event.key]
                    if command == c.CONFIRM:
                        self.cursor_2.confirm = True
                    next_state = c.CHOOSING_POSITION[self.cursor_2.state].get(command)
                    if next_state:
                        self.cursor_2.state = next_state


    def update_cursor(self):
        self.cursor_1.rect.x, self.cursor_1.rect.y = self.cursor_1.state[1]
        self.cursor_2.rect.x, self.cursor_2.rect.y = self.cursor_2.state[1]


    def blit_everything(self, surface):
        surface.blit(self.background, self.background_rect)
        surface.blit(self.cursor_1.image, self.cursor_1.rect)
        surface.blit(self.cursor_2.image, self.cursor_2.rect)


    def check_if_all_confirmed(self):
        if self.cursor_1.confirm and self.cursor_2.confirm:
            self.game_info[c.P1_CHARACTER] = self.cursor_1.state[0]
            self.game_info[c.P2_CHARACTER] = self.cursor_2.state[0]
            self.done = True