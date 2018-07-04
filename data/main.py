from . import tools, setup
from . import constants as c

from .states import main_menu
from .states import gaming
from .states import choosing
from .states import game_over

from multiprocessing import Process,Pipe
import pygame
import time

def choose_pro(name,con1,con2,run_it):
    if name == 'play_music':
        play_music(con1)
    elif name == 'run':
        run_it.main(con2)

def play_music(pipe):
    old = ''
    new = ''
    start = time.time()
    while time.time()-start < 100000:
        if pipe.poll(0.1):
            new = pipe.recv()
        if new != old and new != "":
            if new == 'stop':
                break
            pygame.mixer.music.load(new)
            pygame.mixer.music.play()
            old = new
        time.sleep(1)

def main():
    ( con1, con2) = Pipe()
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {
        c.MAIN_MENU: main_menu.MainMenu(),
        c.CHOOSING: choosing.Choosing(),
        c.GAMING: gaming.Gaming(),
        c.GAME_OVER: game_over.GameOver()
    }
    run_it.setup_states(state_dict, c.MAIN_MENU)
    run_it.main()
