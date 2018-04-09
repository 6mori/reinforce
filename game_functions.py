import sys

import pygame

from brick import Brick

def check_keydown_events( event, character ):
    if event.key == pygame.K_RIGHT:
        character.moving_right = True
    elif event.key == pygame.K_LEFT:
        character.moving_left = True
    elif event.key == pygame.K_UP:
        character.jumping = True
    #elif event.key == pygame.K_SPACE:
    '''
    elif event.key == pygame.K_q:
        sys.exit()
    '''


def check_keyup_events( event, character ):
    if event.key == pygame.K_RIGHT:
        character.moving_right = False
    elif event.key == pygame.K_LEFT:
        character.moving_left = False


def check_events( character ):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events( event, character )
        elif event.type == pygame.KEYUP:
            check_keyup_events( event, character )
        #elif event.type == pygame.MOUSEBUTTONDOWN:


def check_character_bricks_collisions( character, bricks ):
    collisions = pygame.sprite.spritecollide( character, bricks, False )
    downable = True
    leftable = True
    rightable = True
    print(character.drop_speed)

    if collisions:
        for brick in collisions:
            clip_rect =  brick.rect.clip( character )
            if clip_rect.width <= character.run_speed+1 and clip_rect.height <= 2:
                continue
            if clip_rect.bottom >= brick.rect.top+2 and clip_rect.top == brick.rect.top and \
                    clip_rect.width >= character.run_speed+1 :
                downable = False
                character.rect.bottom = brick.rect.top
            if clip_rect.left >= brick.rect.right-character.run_speed-1 and clip_rect.right == brick.rect.right and \
                    clip_rect.height >= brick.rect.height/2:
                leftable = False
                character.rect.left = brick.rect.right
            if clip_rect.right <= brick.rect.left+character.run_speed+1 and clip_rect.left == brick.rect.left and \
                    clip_rect.height >= brick.rect.height/2:
                rightable = False
                character.rect.right = brick.rect.left

    character.not_on_land = downable
    character.no_brick_on_left = leftable
    character.no_brick_on_right = rightable



def check_collisions( character, bricks ):
    check_character_bricks_collisions( character, bricks )


def create_bricks( bricks, x, x_d, y, y_d, settings, screen ):
    for x_i in list(range( x, x_d+1 )):
        for y_i in list(range( y, y_d+1 )):
            bricks.add( Brick( x_i, y_i, settings, screen ) )


def update_characters( character ):
    character.update()


def update_bricks( bricks ):
    bricks.update()


def update_screen( settings, screen, character, bricks ):
    screen.fill( settings.bg_color )
    character.draw()
    for brick in bricks.sprites():
        brick.draw()

    pygame.display.flip()