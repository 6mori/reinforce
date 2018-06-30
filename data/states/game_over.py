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

        self.state = c.PLAY

        print(self.game_info)

        self.setup_background()
        #self.setup_cursor()
        self.setup_UI()

        # For test
        #self.quit = True


    def setup_UI(self):
        self.UI = {}
        self.UI[c.PLAY] = [pg.transform.scale(pg.image.load('images/UI/once_more.png'), (150, 50)),
                           pg.transform.scale(pg.image.load('images/UI/once_more.png'), (180, 60))]
        self.UI[c.QUIT] = [pg.transform.scale(pg.image.load('images/UI/exit_game.png'), (150, 50)),
                           pg.transform.scale(pg.image.load('images/UI/exit_game.png'), (180, 60))]


    def setup_background(self):
        self.background = pg.transform.scale(pg.image.load('images/%s' % c.RESULT_SCREEN), c.SCREEN_SIZE)
        self.background_rect = self.background.get_rect()


    def setup_cursor(self):
        pass
        # self.cursor = pg.sprite.Sprite()
        # self.cursor.image = pg.Surface([c.TITLE_CURSOR_WIDTH, c.TITLE_CURSOR_HEIGHT])
        # # self.cursor.image.set_colorkey(c.BLACK)
        # self.cursor.rect = self.cursor.image.get_rect()
        # self.cursor.rect.x = 350
        # self.cursor.rect.y = 400
        # self.cursor.state = c.PLAY


    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.game_info[c.CURRENT_TIME] = self.current_time
        self.update_cursor(keys)
        self.blit_everything(surface)


    def update_cursor(self, keys):
        if self.state == c.PLAY:
            if keys[pg.K_DOWN]:
                self.state = c.QUIT
            if keys[pg.K_RETURN]:
                self.done = True
        elif self.state == c.QUIT:
            if keys[pg.K_UP]:
                self.state = c.PLAY
            if keys[pg.K_RETURN]:
                self.quit = True


    def blit_everything(self, surface):
        surface.blit(self.background, self.background_rect)
        #surface.blit(self.cursor.image, self.cursor.rect)
        for state in self.UI.keys():
            if state == c.PLAY:
                show_xy = (350, 300)
            if state == c.QUIT:
                show_xy = (350, 450)
            if state == self.state:
                surface.blit(self.UI[state][1], show_xy)
            else:
                surface.blit(self.UI[state][0], show_xy)