import pygame as pg

from .. import tools, setup
from .. import constants as c

class GameOver(tools._State):
    def __init__(self):
        super(GameOver, self).__init__()


    def startup(self, current_time, persist):
        self.game_info = persist
        self.persist = self.game_info

        print(self.game_info)

        # For test
        self.quit = True


    def setup_background(self):
        pass


    def update(self, surface, keys, current_time):
        pass
