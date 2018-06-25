SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
HALF_SCREEN_SIZE = (SCREEN_WIDTH // 2, SCREEN_HEIGHT)

MAP_WIDTH = SCREEN_WIDTH
MAP_HEIGHT = 2000
MAP_SIZE = (MAP_WIDTH, MAP_HEIGHT)

ORIGINAL_CAPTION = "Gayforce"

## COLORS ##

#            R    G    B
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FOREST_GREEN = (31, 162, 35)
BLUE = (0, 0, 255)
SKY_BLUE = (39, 145, 251)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
NEAR_BLACK = (19, 15, 48)
COMBLUE = (233, 232, 255)
GOLD = (255, 215, 0)

BGCOLOR = WHITE

# Game states

MAIN_MENU = 'main menu'
CHOOSING = 'choosing'
LOADING = 'loading'
GAMING = 'gaming'
GAME_OVER = 'game over'

# Character states

STANDING = 'standing'
WALKING = 'walking'
JUMPING = 'jumping'
FALLING = 'falling'
CLIMBING = 'climbing'
SKILLING = 'skilling'
ACTIONING = 'actioning'

# Character command

ACTION = 'action'
SKILL = 'skill'
JUMP = 'jump'
GO_LEFT = 'go left'
GO_RIGHT = 'go right'
GO_DOWN = 'go down'

# Character property

MAX_X_VEL = 6
MAX_Y_VEL = 11
JUMP_VEL = -10
GRAVITY = 1.01
JUMP_GRAVITY = 0.2

# Game info

P1_CHARACTER = 'p1 character'
P2_CHARACTER = 'p2 character'
CURRENT_TIME = 'current time'
P1_HP = 'p1 hp'
P2_HP = 'p2_hp'

KEYBINDING = 'keybinding'

# Brick property

BRICK_WIDTH = 20
BRICK_HEIGHT = 25
BRICK_DUR = 25

# Bullet property

BULLET_DAMAGE = 25
BULLET_VEL = 10
BULLET_WIDTH = 50
BULLET_HEIGHT = 15
BULLET_SIZE = (BULLET_WIDTH, BULLET_HEIGHT)

# For test

BG_COLOR = GRAY

# Sword property

SWORD_DAMAGE = 25
SWORD_WIDTH = 50
SWORD_HEIGHT = 20

# Direction

RIGHT = 'right'
LEFT = 'left'
UP = 'up'
DOWN = 'down'
RIGHT_UP = 'right_up'
RIGHT_DOWN = 'right_down'
LEFT_UP = 'left_up'
LEFT_DOWN = 'left_down'

TITLE_SCREEN = 'title_screen.jpg'
CHOOSING_SCREEN = 'choosing_screen.jpg'
RESULT_SCREEN = 'result_screen.png'

# Main menu options

PLAY = 'play'
QUIT = 'quit'

TITLE_CURSOR_WIDTH = 100
TITLE_CURSOR_HEIGHT = 50
CHOOSING_CURSOR_WIDTH = 50
CHOOSING_CURSOR_HEIGHT = 50

CONFIRM = 'confirm'

# Item property

PROP_MAX_Y_VEL = 10

P1_CHOOSE_BASE = (100, 100)
P2_CHOOSE_BASE = (600, 100)

FPS = 60

# Character name

DARLING = 'Darling'
GUAN_GONG = 'Guan_gong'
K = 'k'
ARCHER = 'Archer'
SPIDER_PRINCE = 'Spider_prince'
POENA = 'Poena'
GHOST = 'Ghost'

CHARACTERS = [
    DARLING,
    GUAN_GONG,
    K,
    ARCHER,
    SPIDER_PRINCE,
    POENA,
    GHOST
]

# Character speeds(higher = slower)

CHARACTER_MOVING_SPEED = {
    'Guan_gong': 6,
    'Darling': 8,
    'k': 6,
    'Archer': 10,
    'Spider_prince': 10,
    'Poena': 8,
    'Ghost': 8
}
# Character size

CHARACTER_SIZE = {
    'Guan_gong': (103 // 3, 200 // 3),
    'Darling': (103 // 3, 131 // 3),
    'k': (75 // 3, 119 // 3),
    'Archer': (103 // 3, 131 // 3),
    'Spider_prince': (103 // 2, 131 // 2),
    'Poena': (69 // 3, 154 // 3),
    'Ghost': (239 // 4, 213 // 4)
}
# Character skill
SKILL_SPEED = {
    'Darling': 10,
    'Guan_gong': 10,
    'k': 5,
    'Archer': 20,
    'Spider_prince': 5,
    'Poena': 10,
    'Ghost': 5
}

# Stand animation
STAND_ANIMATION_SPEED = {
    'Darling': 100,
    'Guan_gong': 8,
    'k': 6,
    'Archer': 100,
    'Spider_prince': 35,
    'Poena': 10,
    'Ghost': 100
}

# Character action_aninamation_speed
ACTION_SPEED = {
    'Darling': 10,
    'Guan_gong': 2,
    'k': 5,
    'Archer': 20,
    'Spider_prince': 10,
    'Poena': 10,
    'Ghost': 2
}

# MP
P1MPPOS = (40, 20)
P2MPPOS = (630, 20)

# Action item type
BULLET = 'bullet'
SWORD = 'sword'

# SCROLL_BRICK = 10
SCROLL_TIME = 6000
SCROLL_LEN = BRICK_HEIGHT

# BGM
TITLE_BGM = 'title.bgm.mp3'
CHOOSING_BGM = 'choosing_bgm.mp3'
GAMING_BGM = 'main_theme.ogg'
