import pygame as pg

from .. import tools, setup
from .. import constants as c


class GameOver(tools._State):
    def __init__(self):
        super(GameOver, self).__init__()

    def startup(self, current_time, persist):
        self.game_info = persist
        self.persist = self.game_info
        self.next = c.CHOOSING

        print(self.game_info)

        self.setup_background()
        self.setup_cursor()

        # For test
        #self.quit = True


    def setup_background(self):
        self.background = pg.transform.scale(pg.image.load('images/%s' % c.RESULT_SCREEN), c.SCREEN_SIZE)
        self.background_rect = self.background.get_rect()


    def setup_cursor(self):
        self.cursor = pg.sprite.Sprite()
        self.cursor.image = pg.Surface([c.TITLE_CURSOR_WIDTH, c.TITLE_CURSOR_HEIGHT])
        # self.cursor.image.set_colorkey(c.BLACK)
        self.cursor.rect = self.cursor.image.get_rect()
        self.cursor.rect.x = 350
        self.cursor.rect.y = 400
        self.cursor.state = c.PLAY


    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.game_info[c.CURRENT_TIME] = self.current_time
        self.update_cursor(keys)
        self.blit_everything(surface)


    def update_cursor(self, keys):
        if self.cursor.state == c.PLAY:
            self.cursor.rect.y = 400
            if keys[pg.K_DOWN]:
                self.cursor.state = c.QUIT
            if keys[pg.K_RETURN]:
                self.done = True
        elif self.cursor.state == c.QUIT:
            self.cursor.rect.y = 450
            if keys[pg.K_UP]:
                self.cursor.state = c.PLAY
            if keys[pg.K_RETURN]:
                self.quit = True


    def blit_everything(self, surface):
        surface.blit(self.background, self.background_rect)
        surface.blit(self.cursor.image, self.cursor.rect)