import pygame as pg

from .. import tools
from .. import constants as c


class MainMenu(tools._State):
    def __init__(self):
        super(MainMenu, self).__init__()

        self.reset_game_info()
        self.startup(0.0, self.persist)

    def startup(self, current_time, persist):
        #self.game_info = persist
        #self.persist = self.game_info

        self.next = c.CHOOSING

        self.setup_background()
        self.setup_cursor()

    def setup_UI(self):
        self.UI = []
        self.UI[0] = pg.image.load('images/UI/start_game.png')
        self.UI[1] = pg.image.load('images/UI/exit_game.png')

    def setup_background(self):
        self.background = pg.transform.scale(pg.image.load('images/%s' % c.TITLE_SCREEN), c.SCREEN_SIZE)
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
                self.reset_game_info()
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


    def get_event(self, event):
        if event.type == pg.KEYUP:
            self.done = True


    def reset_game_info(self):
        self.game_info = {
            c.P1_CHARACTER: '',
            c.P2_CHARACTER: '',
            c.CURRENT_TIME: 0.0,
            c.P1_HP: 0,
            c.P2_HP: 0,
            c.P1_HEART: 0,
            c.P2_HEART: 0,
        }
        self.persist = self.game_info
