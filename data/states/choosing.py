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

        # For test
        self.game_info[c.P1_CHARACTER] = c.DARING
        self.game_info[c.P2_CHARACTER] = c.GUAN
        self.done = True


    def setup_background(self):
        pass


    def update(self, surface, keys, current_time):
        pass
