import os
import pygame as pg

from . import constants as c

direct2pos = {
    c.RIGHT: (50, 0),
    c.LEFT : (-50, 0),
    c.UP   : (0, -50),
    c.DOWN : (0, 50),
}

keybinding = [
    {
        c.ACTION  : pg.K_j,
        c.SKILL   : pg.K_l,
        c.JUMP    : pg.K_w,
        c.GO_LEFT : pg.K_a,
        c.GO_RIGHT: pg.K_d,
        c.GO_DOWN : pg.K_s
    },
    {
        c.ACTION  : pg.K_KP1,
        c.SKILL   : pg.K_KP3,
        c.JUMP    : pg.K_UP,
        c.GO_LEFT : pg.K_LEFT,
        c.GO_RIGHT: pg.K_RIGHT,
        c.GO_DOWN : pg.K_DOWN
    }
]

#砖块种类
kindOfBrick={
    'grass_left':{'name':'images/grass_left.png','dur':25},
    'grass_middle':{'name':'images/grass_middle.png','dur':25 },
    'grass_right': {'name': 'images/grass_right.png', 'dur': 25},
    'grass_inside': {'name': 'images/grass_inside.png', 'dur': 25},
    'long_wood':{'name':'images/long_wood.png', 'dur': 50},
    'long_stone':{'name':'images/long_stone.png', 'dur': 10000},
}

#背景种类
kindOfGround={
    'grass_surface':['grass_left', 'grass_middle', 'grass_right'],
    'grass_soil':['grass_inside', 'grass_inside', 'grass_inside'],
    'long_wood':['long_wood', 'long_wood', 'long_wood'],
    'long_stone':['long_stone', 'long_stone', 'long_stone'],
 }

#道具种类
kindOfProps={
    'Prop_HP_potion':{'name':'images/Prop_HP_potion.png', 'dur': 25},
    'Prop_MP_potion':{'name':'images/Prop_MP_potion.png', 'dur': 25},
    'Prop_HP_Apple':{'name':'images/Prop_HP_Apple.png', 'dur': 25},
    'Prop_HP_Ginseng':{'name':'images/Prop_HP_Ginseng.png', 'dur': 25},
    'Prop_Shoe':{'name':'images/shoe.png', 'dur': 25},
    'Prop_Corselet':{'name':'images/Prop_Corselet.png', 'dur': 25},
}

class Control(object):
    ''' Control object for entire project '''
    def __init__(self, caption):
        self.screen = pg.display.get_surface()
        self.done = False
        self.clock = pg.time.Clock()
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()
        self.caption = caption
        self.state_dict = {}
        self.state_name = None
        self.state = None

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

        # For test
        persist = self.state.cleanup()
        self.state.startup(self.current_time, persist)

    def update(self):
        self.current_time = pg.time.get_ticks()
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, self.keys, self.current_time)

    def flip_state(self):
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)
        self.state.previous = previous

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
            self.state.get_event(event)

    def main(self):
        while not self.done:
            self.event_loop()
            self.update()
            pg.display.update()
            self.clock.tick(c.FPS)
            print(self.clock.get_fps())


class _State(object):
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.persist = {}

    def get_event(self, event):
        pass

    def startup(self, current_time, persistant):
        self.persist = persistant
        self.start_time = current_time

    def cleanup(self):
        self.done = False
        return self.persist

    def update(self, surface, keys, current_time):
        pass


def load_all_music(directory, accept=('.wav', '.mp3', '.ogg', '.mdi', '.flac')):
    songs = {}
    for song in os.listdir(directory):
        name,ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    print(songs.values())
    return songs