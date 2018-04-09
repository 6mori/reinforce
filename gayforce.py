import pygame
from pygame.sprite import Group

from settings import Settings
from character import Character
import game_functions as gf

def run_game():
    # initial window
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode( ( settings.screen_width, settings.screen_height ) )
    pygame.display.set_caption( 'GayForce' )

    # initial objects
    character = Character( 500, 100, settings, screen )
    bricks = Group()
    gf.create_bricks( bricks, 0, 35, 20, 20, settings, screen )
    gf.create_bricks( bricks, 0, 80, 30, 30, settings, screen )
    gf.create_bricks( bricks, 40, 45, 0, 20, settings, screen )
    gf.create_bricks( bricks, 40, 45, 25, 40, settings, screen )

    while True:
        gf.check_events( character )

        gf.update_characters( character )

        gf.update_bricks( bricks )

        gf.check_collisions(character, bricks)

        gf.update_screen( settings, screen, character, bricks )

run_game()