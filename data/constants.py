SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

ORIGINAL_CAPTION = "Gayforce"

## COLORS ##

#            R    G    B
GRAY         = (100, 100, 100)
NAVYBLUE     = ( 60,  60, 100)
WHITE        = (255, 255, 255)
RED          = (255,   0,   0)
GREEN        = (  0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)
BLUE         = (  0,   0, 255)
SKY_BLUE     = ( 39, 145, 251)
YELLOW       = (255, 255,   0)
ORANGE       = (255, 128,   0)
PURPLE       = (255,   0, 255)
CYAN         = (  0, 255, 255)
BLACK        = (  0,   0,   0)
NEAR_BLACK   = ( 19,  15,  48)
COMBLUE      = (233, 232, 255)
GOLD         = (255, 215,   0)

BGCOLOR = WHITE

# Game states

MAIN_MENU = 'main menu'
CHOOSING  = 'choosing'
LOADING   = 'loading'
GAMING    = 'gaming'
GAME_OVER = 'game over'

# Character states

STANDING = 'standing'
WALKING  = 'walking'
JUMPING  = 'jumping'
FALLING  = 'falling'
CLIMBING = 'climbing'
SKILLING = 'skilling'

# Character command

ACTION   = 'action'
SKILL    = 'skill'
JUMP     = 'jump'
GO_LEFT  = 'go left'
GO_RIGHT = 'go right'
GO_DOWN  = 'go down'

# Character property

MAX_X_VEL    = 1
MAX_Y_VEL    = 11
JUMP_VEL     = -2.51
GRAVITY      = 0.05
JUMP_GRAVITY = 0.02

# Player1 property

P1_DAMAGE = 2

# Game info

P1_CHARACTER = 'p1 character'
P2_CHARACTER = 'p2 character'
CURRENT_TIME = 'current time'
P1_HP = 'p1 hp'
P2_HP = 'p2_hp'

KEYBINDING   = 'keybinding'

# Brick property

BRICK_WIDTH  = 20
BRICK_HEIGHT = 25
BRICK_DUR    = 25

# Bullet property

BULLET_VEL    = 1
BULLET_WIDTH  = 50
BULLET_HEIGHT = 10
BULLET_SIZE   = (50,10)

# For test

BG_COLOR = GRAY

#Character speeds(higher = slower)

CHARACTER_MOVING_SPEED = 25


#Character size

CHARACTER_SIZE = {
    'Guan_gong' : (103 // 3, 250 // 3),
    'Darling' : (103 // 3, 131 // 3),
    'k' : (75 // 3, 119 // 3),
    'Archer' : (103 // 3, 131 // 3)
}


#Character skill
SKILL_SPEED = {
    'Darling' : 10,
    'Guan_gong' : 20,
    'k' : 20,
    'Archer': 20
}


#Stand animation
STAND_ANIMATION_SPEED = {
    'Darling' : 100,
    'Guan_gong' : 30,
    'k' : 50,
    'Archer': 100
}

# Sword property

SWORD_WIDTH  = 50
SWORD_HEIGHT = 20

# Character name

DARLING = 'Darling'
GUAN_GONG   = 'Guan_gong'
K   = 'k'
ARCHER =  'Archer'

# Direction

RIGHT      = 'right'
LEFT       = 'left'
UP         = 'up'
DOWN       = 'down'
RIGHT_UP   = 'right_up'
RIGHT_DOWN = 'right_down'
LEFT_UP    = 'left_up'
LEFT_DOWN  = 'left_down'

#

TITLE_SCREEN = 'title_screen'
CHOOSING_SCREEN = 'choosing_screen'

# Main menu options

PLAY = 'play'
QUIT = 'quit'

# Choosing absolute position

P1_DARLING = (DARLING, (100, 100))
P1_GUAN_GONG = (GUAN_GONG, (100, 150))
P1_K = (K, (150, 100))
P1_ARCHER = (ARCHER, (150, 150))
P2_DARLING = (DARLING, (600, 100))
P2_GUAN_GONG = (GUAN_GONG, (600, 150))
P2_K = (K, (650, 100))
P2_ARCHER = (ARCHER, (650, 150))

# Choosing relative position

CHOOSING_POSITION = {
    P1_DARLING: {
        DOWN: P1_GUAN_GONG,
        RIGHT: P1_K,
    },
    P1_GUAN_GONG: {
        UP: P1_DARLING,
        RIGHT: P1_ARCHER,
    },
    P1_K: {
        LEFT: P1_DARLING,
        DOWN: P1_ARCHER
    },
    P1_ARCHER: {
        LEFT: P1_GUAN_GONG,
        UP: P1_K
    },

    P2_DARLING : {
        DOWN: P2_GUAN_GONG,
        RIGHT: P2_K,
    },
    P2_GUAN_GONG : {
        UP: P2_DARLING,
        RIGHT: P2_ARCHER
    },
    P2_K : {
        LEFT: P2_DARLING,
        DOWN: P2_ARCHER,
    },
    P2_ARCHER: {
        LEFT: P2_GUAN_GONG,
        UP: P2_K
    },
}

TITLE_CURSOR_WIDTH = 100
TITLE_CURSOR_HEIGHT = 50
CHOOSING_CURSOR_WIDTH = 50
CHOOSING_CURSOR_HEIGHT = 50

CONFIRM = 'confirm'

# Item property

PROP_MAX_Y_VEL = 10