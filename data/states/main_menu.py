import pygame as pg

from .. import tools, setup
from .. import constants as c

class MainMenu(tools._State):
    def __init__(self):
        super(MainMenu, self).__init__()

        persist = {
            c.P1_CHARACTER: '',
            c.P2_CHARACTER: '',
            c.CURRENT_TIME: 0.0,
            c.P1_HP: '',
            c.P2_HP: '',
        }
        self.startup(0.0, persist)


    def startup(self, current_time, persist):
        self.game_info = persist
        self.persist = self.game_info

        self.next = c.CHOOSING

        self.setup_background()


    def setup_background(self):
        pass


    def update(self, surface, keys, current_time):
        pass


    def get_event(self, event):
        if event.type == pg.KEYUP:
            self.done = True